from datetime import datetime

from view.data.user import User
from view.enum.event_label import Label, EventLabels
from view.enum.event_state import EventStates

from view.util import trim_microseconds


class Event:
    """
    Special event, displaying on calendar
    """

    def __init__(self, id: int, title: str, start_datetime: datetime, label: Label = EventLabels.LESSON, url=""):
        self.id = id
        self.title = title
        self.start_datetime = start_datetime

        self.label = label
        self.url = url

        self.description = ""
        self.description_short = ""

        self.participant_list = []
        self.max_participants = 10

        self.wait_list = []

        self.results = []

        self.state = EventStates.NOT_READY

        self.priority = 0

    def __repr__(self):
        return "{name: " + str(self.title) + "}"

    def has_participant(self, user: User):
        return user in self.participant_list

    def has_waiter(self, user: User):
        return user in self.wait_list

    @property
    def start_date(self):
        return self.start_datetime.date()

    @property
    def start_time(self):
        return trim_microseconds(self.start_datetime).time()

    @property
    def short_name(self):
        return self.title[0:6] + " ..."


class EventResult:
    def __init__(self, user_name: str = "", profile_url: str = "", place: int = 0, reward: int = 0):
        self.user_name = user_name
        self.profile_url = profile_url
        self.place = place
        self.reward = reward
