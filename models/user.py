from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType, force_auto_coercion
from enums.enums import Gender
from router import db

from models.event_result import EventResult

force_auto_coercion()

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(PasswordType(
        schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']
    ))

    gender = db.Column(db.String(80), default=Gender.MALE.name)

    xp = db.Column(db.Integer, default=0)

    image_big = db.Column(db.String(120), default="static/img/male256.png")

    role = db.Column(db.String(80), default="User")

    events_history = relationship("EventResult", backref="user", lazy='dynamic')

    def __repr__(self):
        return "<User %r>" % self.login