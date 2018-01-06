from typing import List

from view.data.event_result import EventResult


class View:
    def __init__(self, events_history: List[EventResult]):
        self.events_history = events_history

        self.min_width = 400
        self.max_width = 1200
