from calendar import Calendar
from datetime import date

from view.data.day import DayData
from view.data.event import EventData
from view.data.pass_card import PassCardData
from view.enum.event_label import EventLabels
from view.error import Error
from view.loc import Loc


class MonthData:
    """
    Single month of Days. Use it instead of whole year
    """

    def __init__(self, now: date):
        self.id = now.month
        self.loc_key = Loc.MONTHS[self.id - 1]

        self.year = now.year

        c = Calendar()
        self.days = list(
            map(lambda d: DayData(d), c.itermonthdates(now.year, now.month))
        )

        self.today = next(d for d in self.days if d.date == now)

        self.events = []

    def add_event(self, event: EventData):
        event_start_date = event.start_datetime.date()

        try:
            event_day = next(d for d in self.days if d.date == event_start_date)
        except StopIteration:
            raise Error("No day " + str(event_start_date) + " in " + str(self.year) + "-" + str(self.id))

        event_day.events.append(event)

        self.events.append(event)

    def apply_pass_card(self, pass_card: PassCardData):
        for d in self.days:
            if d.date in pass_card.days:
                d.label = EventLabels.PASS_CARD
