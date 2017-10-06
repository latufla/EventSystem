from flask import request, render_template, session, redirect, url_for

from enums.enums import UserRole
from models.event import Event
from models.forms.register_form import RegisterForm

from models.user import User


class Controller:
    def __init__(self, app, db):
        self.app = app
        self.db = db

    @classmethod
    def getUser(cls):
        return User.query.filter_by(login=session["login"]).first()

    def registerUser(self):
        form = RegisterForm(request.form)

        # inv = str(form.invite.data)
        # if not self.invites.tryUseInvite(inv):
        #     error = "Неправильный или использованный инвайт"
        #     return render_template("register.html", error=error)

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

