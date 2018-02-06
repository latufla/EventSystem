from typing import List

from view.data.event_history_record import EventHistoryRecordData


class EventsHistoryView:
    def __init__(self, events_history: List[EventHistoryRecordData]):
        self.events_history = events_history

        self.min_width = 400
        self.max_width = 1200
