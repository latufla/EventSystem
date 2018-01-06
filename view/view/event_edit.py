from typing import List

from view.data.event import Event
from view.enum.event_label import Label


class View:
    def __init__(self, event: Event, save_url: str, label_config: List[Label]):
        self.event = event

        self.save_url = save_url
        self.label_config = label_config

        self.min_width = 400
        self.max_width = 1200
