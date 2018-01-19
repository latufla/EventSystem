from view.data.event import Event
from view.enum.event_state import EventStates


class View:
    def __init__(self, event: Event, creator: bool, add_participant_url: "", remove_participant_url: ""):
        self.event = event
        self.creator = creator

        self.add_participant_url = add_participant_url
        self.remove_participant_url = remove_participant_url

        self.event_states = EventStates

        self.min_width = 700
        self.max_width = 4000

    @property
    def can_show_results(self):
        return len(self.event.results) and (self.event.state == EventStates.FINISHED
                                            or self.event.state == EventStates.REWARDED)
