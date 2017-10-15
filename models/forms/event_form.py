from wtforms import StringField, IntegerField, FieldList

from wtforms.ext.dateutil.fields import DateTimeField

from models.forms.form_base import FormBase


class EventForm(FormBase):
    title = StringField()

    description_short = StringField()
    description = StringField()

    max_participants = IntegerField()
    participants = FieldList(StringField())

    rewards = FieldList(IntegerField())
    best_player_reward = IntegerField()

    date_start = DateTimeField(display_format='%d/%m/%Y %H:%M')

    image_big = StringField()
