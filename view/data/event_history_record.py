from view.data.event import Event


class EventHistoryRecord:
    def __init__(self, event: Event, place: int = 0, reward: int = 0, rewarded: bool = False):
        self.event = event
        self.place = place
        self.reward = reward
        self.rewarded = rewarded
