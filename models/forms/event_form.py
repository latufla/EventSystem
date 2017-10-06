from wtforms import Form, StringField, IntegerField, FieldList

from wtforms.ext.dateutil.fields import DateTimeField


class EventForm(Form):
    title = StringField()

    description_short = StringField()
    description = StringField()

    max_participants = IntegerField()
    participants = FieldList(StringField())

    rewards = FieldList(IntegerField())
    best_player_reward = IntegerField()

    date_start = DateTimeField(display_format='%d/%m/%Y %H:%M')

    image_big = StringField()
