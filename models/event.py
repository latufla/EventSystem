from router import db

from models.event_result import EventResult
from models.user import User
from enums.enums import EventStatus


event_participate = db.Table('event_participate', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

event_wait = db.Table('event_wait', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User")

    title = db.Column(db.String(80))
    description_short = db.Column(db.String(80))
    description = db.Column(db.String(120))

    max_participants = db.Column(db.Integer, default=10)

    participants = db.relationship("User", secondary=event_participate, lazy='dynamic', backref=db.backref("events_participate", lazy='dynamic'))
    wait_list = db.relationship("User", secondary=event_wait, lazy='dynamic', backref=db.backref("events_wait", lazy='dynamic'))

    status = db.Column(db.String(80), default=EventStatus.NOT_READY.name)

    # rewards = ListField()
    best_player_reward = db.Column(db.Integer, default=0)

    result_file = db.Column(db.String(120))
    results = db.relationship("EventResult", backref="event", lazy='dynamic')

    date_start = db.Column(db.DateTime)

    image_big = db.Column(db.String(120), default="//localhost:5000/static/img/event.png")

    published = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Event %r>" % self.title