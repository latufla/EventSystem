from flask import request, render_template, session, redirect, url_for

from enums.enums import UserRole
from models.event import Event
from models.forms.event_form import EventForm
from models.forms.register_form import RegisterForm

from models.user import User
from services.invite_service import InviteService


class Controller:
    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.invites = InviteService()

    @classmethod
    def getUser(cls):
        return User.query.filter_by(login=session["login"]).first()

    def registerUser(self):
        form = RegisterForm(request.form)

        inv = str(form.invite.data)
        if not self.invites.tryUseInvite(inv):
            error = "Неправильный или использованный инвайт"
            return render_template("register.html", error=error)

        if form.validate():
            user = User(
                login=form.login.data,
                password=str(form.password.data),
                gender=form.gender.data
            )

            user.image_big = "static/img/male256.png"
            if user.gender == "Female":
                user.image_big = "static/img/female256.png"

            self.db.session.add(user)
            self.db.session.commit()

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
            if password == password_candidate:
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

    def getUserProfile(self):
        login = session["login"]
        user = User.query.filter_by(login=login).first()
        if user is None:
            return redirect(url_for('login'))

        return render_template('profile.html', user=user)

    def getCreatedEvents(self):
        user = self.getUser()
        if user is None:
            return redirect(url_for('login'))

        events = user.events_created.order_by('date_start')
        return render_template('events.html', user=user, events=events, created=True)


    def getPublishedEvents(self):
        user = self.getUser()
        if user is None:
            return redirect(url_for('login'))

        events = user.events_participate.filter_by(published=True).order_by('date_start')
        return render_template('events.html', user=user, events=events)


    def getParticipateEvents(self):
        user = self.getUser()
        if user is None:
            return redirect(url_for('login'))

        events = user.events_participate.all()
        return render_template('events.html', user=user, events=events, participate=True)

    def getInvites(self):
        if request.method == 'POST':
            self.invites.createInvites(100, 10)
            return redirect(url_for('invites'))

        user = self.getUser()
        invites = self.invites.getInvites()
        return render_template('invites.html', user=user, invites=invites)

    def createEvent(self):
        if request.method == 'GET':
            user = self.getUser()
            return render_template("event_create.html", user=user, image_big="static/img/event.png")

        if request.method == 'POST':
            form = EventForm(request.form)

            rewards = request.form.getlist("rewards")
            for r in rewards:
                if r:
                    form.rewards.append_entry(r)

            if form.validate():
                user = self.getUser()

                event = Event(
                    author_id=user.id,

                    title=form.title.data,
                    description_short=form.description_short.data,
                    description=form.description.data,

                    date_start=form.date_start.data,

                    max_participants=form.max_participants.data,

                    # rewards=form.rewards.data,
                    best_player_reward=form.best_player_reward.data
                )

                self.db.session.add(event)
                self.db.session.commit()

            return redirect(url_for("events"))
