from EventSystem import db
from enums.enums import EventStatus


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User")

    title = db.Column(db.String(80))
    description_short = db.Column(db.String(80))
    description = db.Column(db.String(120))

    max_participants = db.Column(db.Integer, default=10)

    # participants = ListField()
    # wait_list = ListField()

    status = db.Column(db.String(80), default=EventStatus.NOT_READY.name)

    # rewards = ListField()
    best_player_reward = db.Column(db.Integer, default=0)

    # results = ListField(EmbeddedDocumentField(EventResult))
    # result_file = StringField()

    # date_start = DateTimeField()

    image_big = db.Column(db.String(120), default="//localhost:5000/static/img/event.png")

    published = db.Column(db.Boolean, default=False)
