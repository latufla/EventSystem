from wtforms import StringField, PasswordField, validators

from models.forms.form_base import FormBase


class EditSettingsForm(FormBase):
    login = StringField('Login', [validators.length(min=1, max=20)])
    password = PasswordField('Password', [
        validators.length(min=3, max=20, message='Пароль должен быть не меньше 3х символов'),
        validators.DataRequired(),
        validators.equal_to('confirm', message='Пароли не совпадают')
    ])
    confirm = PasswordField('Confirm')
    gender = StringField('Gender')


class EditSettingsNoPasswordForm(FormBase):
    login = StringField('Login', [validators.length(min=1, max=20)])
    gender = StringField('Gender')