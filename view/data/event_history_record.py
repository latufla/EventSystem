from view.data.event import EventData


class EventHistoryRecordData:
    def __init__(self, event: EventData, place: int = 0, reward: int = 0, rewarded: bool = False):
        self.event = event
        self.place = place
        self.reward = reward
        self.rewarded = rewarded
