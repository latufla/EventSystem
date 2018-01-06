from view.loc import Loc


class EventState:
    def __init__(self, loc_key: str, color: str = None):
        self.loc_key = loc_key
        self.color = color


class EventStates:
    NOT_READY = EventState(Loc.NOT_READY_EVENT_STATE, "grey")
    STARTED = EventState(Loc.STARTED_EVENT_STATE, "green")
    FINISHED = EventState(Loc.FINISHED_EVENT_STATE, "orange")
    REWARDED = EventState(Loc.REWARDED_EVENT_STATE, "red")