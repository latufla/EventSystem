from typing import List

from view.data.event_result import EventResult
from view.data.player import Player


class View:
    def __init__(self, player: Player, events_history: List[EventResult]):
        self.player = player
        self.events_history = events_history
