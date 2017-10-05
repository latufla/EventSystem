from EventSystem import db


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(10))

    def __repr__(self):
        return "<Invite %r>" % self.key