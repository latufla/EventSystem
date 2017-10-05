from sqlalchemy import Integer, Table, Column, ForeignKey
from sqlalchemy_utils import PasswordType, force_auto_coercion

from EventSystem import db
from enums.enums import Gender
from models import event_result

force_auto_coercion()

events_participate = Table('events_participate', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('event_id', Integer, ForeignKey('event.id'))
)

events_history = Table('events_history', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('event_id', Integer, ForeignKey('event.id'))
)

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

    events_participate = db.relationship("Event", secondary=events_participate, lazy='dynamic')

    events_history = db.relationship("EventResult", backref="user", lazy='dynamic')

    def __repr__(self):
        return "<User %r>" % self.login