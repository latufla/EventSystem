from initter import db


class EventResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column('event_id', db.Integer, db.ForeignKey('event.id'))

    place = db.Column('place', db.Integer)
    reward = db.Column('reward', db.Integer)
    rewarded = db.Column('rewarded', db.Boolean)

    def __repr__(self):
        return "<EventResult %r>" % self.id