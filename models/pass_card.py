from initter import db

from models.user import User
from models.event import Event

pass_card_use = db.Table('pass_card_use', db.Model.metadata,
                         db.Column('pass_card_id', db.Integer, db.ForeignKey('pass_card.id')),
                         db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
                         )


class PassCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    start_date = db.Column(db.DateTime)
    expire_date = db.Column(db.DateTime)

    events_max_count = db.Column(db.Integer, default=8)

    events_visited = db.relationship("PassCard", secondary=pass_card_use, lazy='dynamic')

