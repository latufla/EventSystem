from typing import List

from view.data.event_result import EventHistoryRecord
from view.data.user import User
from view.enum.event_state import EventStates


class View:
    def __init__(self, user: User, events_history: List[EventHistoryRecord], admin: bool = False, myself: bool = True,
                 change_avatar_url: str = "", event_states: EventStates = EventStates):
        self.user = user
        self.events_history = events_history

        self.admin = admin
        self.myself = myself
        self.change_avatar_url = change_avatar_url

        self.event_states = event_states

        self._active_events = list(filter(lambda e: e.event.state == EventStates.NOT_READY
                                                    or e.event.state == EventStates.STARTED, self.events_history))

        # waiter or participant ok
        self._active_events = list(filter(lambda e: e.event.has_waiter(user) or e.event.has_participant(user), self._active_events))


        self._finished_events = list(filter(lambda e: e.event.state == EventStates.FINISHED
                                                      or e.event.state == EventStates.REWARDED, self.events_history))

        # skip if you are waiter
        self._finished_events = list(filter(lambda e: e.event.has_participant(user), self._finished_events))

    def order_history(self):
        self.events_history = sorted(self.events_history, key=lambda e: e.event.start_datetime, reverse=True)

    @property
    def active_events(self):
        return self._active_events

    @property
    def finished_events(self):
        return self._finished_events
