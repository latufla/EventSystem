from typing import List

from view.data.month import MonthData
from view.data.pass_card import PassCardData
from view.enum.event_label import Label


class Tabs:
    CALENDAR = "calendar_tab"
    EVENT_LIST = "event_list_tab"
    PASS_CARD = "pass_card_tab"


class CalendarView:
    def __init__(self, month: MonthData, pass_card: PassCardData, label_config: List[Label], prev_url: str, next_url: str):
        self.month = month
        self.pass_card = pass_card

        self.label_config = label_config

        self.prev_url = prev_url
        self.next_url = next_url

        self.active_tab = Tabs.CALENDAR
        self.min_width = 800
        self.max_width = 1100
