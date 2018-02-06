from typing import List

from view.data.event import EventData
from view.enum.event_label import Label


class EventEditView:
    def __init__(self, event: EventData, save_url: str, label_config: List[Label]):
        self.event = event

        self.save_url = save_url
        self.label_config = label_config

        self.min_width = 400
        self.max_width = 1200
