from flask import request, render_template, session, redirect, url_for

from enums.enums import UserRole
from models.forms.register_form import RegisterForm

import models.user


def registerUser(db):
    form = RegisterForm(request.form)

    # inv = str(form.invite.data)
    # if not self.invites.tryUseInvite(inv):
    #     error = "Неправильный или использованный инвайт"
    #     return render_template("register.html", error=error)

    if form.validate():
        user = models.user.User(
            login=form.login.data,
            password=str(form.password.data),
            gender=form.gender.data
        )

        user.image_big = "static/img/male256.png"
        if user.gender == "Female":
            user.image_big = "static/img/female256.png"

        db.session.add(user)
        db.session.commit()

        session["logged_in"] = True
        session["login"] = user.login
        session["admin"] = user.role == UserRole.ADMIN.name

        return redirect(url_for('register'))

    return render_template('register.html')
