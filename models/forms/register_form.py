from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    login = StringField('Login', [validators.length(min=1, max=20)])
    password = PasswordField('Password', [
        validators.length(min=3, max=20),
        validators.DataRequired(),
        validators.equal_to('confirm', message='Пароли не совпадают')
    ])
    confirm = PasswordField('Confirm')
    gender = StringField('Gender')

    invite = PasswordField('Invite')