from initter import db


class UnregisteredPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="unregistered_password")

    password = db.Column(db.String(10))
