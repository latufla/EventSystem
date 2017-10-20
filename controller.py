from flask import request, render_template, session, redirect, url_for, abort
from sqlalchemy_utils import Password
from sqlalchemy_utils.types.password import passlib

from enums.enums import UserRole, EventStatus, Gender
from models.event import Event
from models.forms.edit_settings_form import EditSettingsForm, EditSettingsNoPasswordForm
from models.forms.event_form import EventForm
from models.forms.register_form import RegisterForm
from models.user import User
from services.invite_service import InviteService
from services.media_service import MediaService
from services.reward_service import RewardService
from tools.db_wrapper import DBWrapper


class Controller:
    def __init__(self, app, db):
        self.app = app
        self.db = DBWrapper(db)
        self.invites = InviteService(self.db)
        self.media = MediaService(app)
        self.rewards = RewardService(self.db)

    @classmethod
    def _getUser(cls):
        return User.query.filter_by(login=session["login"]).first()

    @classmethod
    def _getEvent(cls, event_id):
        return Event.query.filter_by(id=event_id).first()

    def registerInvite(self):
        if request.method == 'POST':
            if 'invite' in request.form:
                invite = request.form["invite"]
                if self.invites.hasInvite(invite):
                    session["invite"] = invite
                    return redirect(url_for("register"))
                else:
                    error = "Неправильный или использованный инвайт"
                    return render_template("register_invite.html", error=error)

        return render_template("register_invite.html")

    def registerUser(self):
        if "invite" not in session:
            return redirect(url_for("register_invite"))

        invite = session["invite"]

        form = RegisterForm(request.form)

        login = str(form.login.data)
        user = User.query.filter_by(login=login).first()
        if user is not None:
            error = "Такой юзер уже существует"
            return render_template("register.html", error=error)

        if not self.invites.tryUseInvite(invite):
            error = "Неправильный или использованный инвайт"
            return render_template("register.html", error=error)
        else:
            session.pop("invite")

        if form.validate():
            user = User(
                login=form.login.data,
                password=str(form.password.data),
                gender=form.gender.data
            )

            user.image_big = "static/img/male256.png"
            if user.gender == "Female":
                user.image_big = "static/img/female256.png"

            self.db.add(user)
            self.db.commit()

            session["logged_in"] = True
            session["login"] = user.login
            session["admin"] = user.role == UserRole.ADMIN.name

            return redirect(url_for('index'))

        return render_template('register.html')

    def loginUser(self):
        login = request.form['login']
        password_candidate = request.form['password']

        user = User.query.filter_by(login=login).first()
        if user is not None:
            password = user.password
            if not password:
                unregistered_password = user.unregistered_password.password
                password = unregistered_password

            if password == password_candidate:
                user.password = password
                if user.unregistered_password:
                    self.db.delete(user.unregistered_password)

                self.db.commit()

                session["logged_in"] = True
                session["login"] = login
                session["admin"] = user.role == UserRole.ADMIN.name
                return redirect(url_for("index"))
            else:
                error = "Wrong password"
                return render_template("login.html", error=error)
        else:
            error = "No user"
            return render_template("login.html", error=error)

    def logoutUser(self):
        session.clear()
        return redirect(url_for('login'))

    def getIndex(self):
        user = self._getUser()
        return redirect(url_for('profile', user_name=user.login))

    def getUserProfile(self, user_name):
        user = User.query.filter_by(login=user_name).first()
        if user is None:
            user = self._getUser()
            return redirect(url_for('profile', user_name=user.login))

        return self._renderUserTemplate('profile.html', user=user)

    def getAllUsers(self):
        users = User.query.all()
        return self._renderUserTemplate('all_users.html', users=users)

    def getCreatedEvents(self):
        user = self._getUser()
        events = user.events_created.order_by('date_start')
        return self._renderUserTemplate('events.html', events=events, created=True)

    def getPublishedEvents(self):
        events = Event.query.filter_by(published=True).order_by('date_start')
        return self._renderUserTemplate('events.html', events=events)

    def getParticipateEvents(self):
        user = self._getUser()
        events_participate = user.events_participate.all()
        events_wait = user.events_wait.all()
        events = events_participate + events_wait
        return self._renderUserTemplate('events.html', events=events, participate=True)

    def getInvites(self):
        if request.method == 'POST':
            self.invites.createInvites(100, 10)
            return redirect(url_for('invites'))

        invites = self.invites.getInvites()
        return self._renderUserTemplate('invites.html', invites=invites)

    def createEvent(self):
        if request.method == 'GET':
            return self._renderUserTemplate("event_create.html", image_big="static/img/event.png")

        if request.method == 'POST':
            form = EventForm(request.form)

            rewards = request.form.getlist("rewards")
            for r in rewards:
                if r:
                    form.rewards.append_entry(r)

            if form.validate():
                user = self._getUser()

                event = Event(
                    author_id=user.id,

                    title=form.title.data,
                    description_short=form.description_short.data,
                    description=form.description.data,

                    date_start=form.date_start.data,

                    max_participants=form.max_participants.data,

                    best_player_reward=form.best_player_reward.data
                )

                event.rewards = []
                rewards = form.rewards.data
                for r in rewards:
                    event.rewards.append(int(r))

                self.db.add(event)
                self.db.commit()

            return redirect(url_for("events"))

    def getEvent(self, event_id):
        event = self._getEvent(event_id)
        if event is None:
            return abort(404)

        return self._renderUserTemplate('event.html', event=event)

    def participateEvent(self, event_id):
        if request.method == 'POST':
            event = self._getEvent(event_id)

            if event is not None:
                user = self._getUser()
                event.wait_list.append(user)

                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def leaveEvent(self, event_id):
        if request.method == 'POST':
            event = self._getEvent(event_id)

            if event is not None:
                user = self._getUser()

                users = event.participants.all()
                for u in users:
                    if u.id == user.id:
                        event.participants.remove(u)
                        break

                users = event.wait_list.all()
                for u in users:
                    if u.id == user.id:
                        event.wait_list.remove(u)
                        break

                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def publishEvent(self, event_id):
        if request.method == 'POST':
            event = self._getEvent(event_id)

            if event is not None:
                event.published = True
                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def unpublishEvent(self, event_id):
        if request.method == 'POST':
            event = self._getEvent(event_id)

            if event is not None:
                event.published = False
                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def changeEventState(self):
        if 'event_id' not in request.form \
                or 'status' not in request.form:
            return ""

        event_id = request.form["event_id"]
        status = request.form["status"]

        event = self._getEvent(event_id)

        if event is not None:
            if EventStatus.HasName(status):
                event.status = status

                if status != EventStatus.REWARDED.name:
                    results = event.results.all()
                    self.db.delete(results)

                if status == EventStatus.FINISHED.name:
                    result_file = self.media.uploadExcel(request.files["result"])
                    event.result_file = result_file
                    self.rewards.collectResults(event, self.invites)

                elif status == EventStatus.REWARDED.name:
                    self.rewards.giveRewards(event)

                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def addParticipantToEvent(self):
        if 'event_id' not in request.form \
                or 'user_id' not in request.form:
            return ""

        event_id = request.form['event_id']
        user_id = request.form['user_id']

        event = self._getEvent(event_id)

        if event is not None:
            user = User.query.filter_by(id=user_id).first()

            if user is not None:
                users = event.participants.all()
                if user not in users:
                    event.participants.append(user)

                users = event.wait_list.all()
                if user in users:
                    event.wait_list.remove(user)

                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def removeParticipantFromEvent(self):
        if 'event_id' not in request.form \
                or 'user_id' not in request.form:
            return ""

        event_id = request.form['event_id']
        user_id = request.form['user_id']

        event = self._getEvent(event_id)

        if event is not None:
            user = User.query.filter_by(id=user_id).first()

            if user is not None:
                users = event.participants.all()
                if user in users:
                    event.participants.remove(user)

                users = event.wait_list.all()
                if user not in users:
                    event.wait_list.append(user)

                self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def uploadAvatar(self):
        if request.method == 'POST':
            files = request.files

            if 'image' in files:
                image_big = self.media.uploadImage(files['image'])

                if image_big is not None:
                    user = self._getUser()
                    user.image_big = image_big

                    self.db.commit()

        return redirect(url_for('profile'))

    def uploadEventAvatar(self, event_id):
        if request.method == 'POST':
            files = request.files

            if 'image' in files:
                image_big = self.media.uploadImage(files['image'])

                if image_big is not None:
                    event = self._getEvent(event_id)

                    if event is not None:
                        event.image_big = image_big
                        self.db.commit()

        return redirect(url_for('event', event_id=event_id))

    def getSettings(self):
        user = self._getUser()
        if request.method == "POST":

            other_user = User.query.filter_by(login=request.form["login"]).first()
            if other_user is not None and user != other_user:
                error = "Такой юзер уже существует"
                return self._renderUserTemplate("settings.html", error=error)

            if request.form["password"]:
                form = EditSettingsForm(request.form)
                if form.validate():
                    user.login = str(form.login.data)
                    user.password = str(form.password.data)

                    user.gender = 'Male'

                    gender = str(form.gender.data)
                    if gender == 'Male':
                        user.gender = Gender.MALE.name
                else:
                    return self._renderUserTemplate("settings.html", error=form.errors_str())
            else:
                form = EditSettingsNoPasswordForm(request.form)
                if form.validate():
                    user.login = str(form.login.data)

                    user.gender = 'Male'

                    gender = str(form.gender.data)
                    if gender == 'Male':
                        user.gender = Gender.MALE.name
                else:
                    return self._renderUserTemplate("settings.html", error=form.errors_str())

            self.db.commit()

            session["login"] = user.login

        return self._renderUserTemplate('settings.html')

    @staticmethod
    def _errorsToString(form):
        error = ""
        for k, v in form.errors.items():
            error += v[0] + '\n'
        return

    def _renderUserTemplate(self, path: str, **kwargs: object):
        viewer = self._getUser()
        if 'user' not in kwargs:
            return render_template(path, viewer=viewer, user=viewer, **kwargs)

        return render_template(path, viewer=viewer, **kwargs)
