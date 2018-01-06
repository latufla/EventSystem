from calendar import Calendar
from datetime import date, timedelta


class PassCard:
    """
    Pass card for variable amount of days
    """

    def __init__(self, start_date: date, days: int, max_events_visited: int):
        self.start_date = start_date
        self.expire_date = self.start_date + timedelta(days=days)

        self.events_visited = []
        self.max_events_visited = max_events_visited

        c = Calendar()

        start_month = list(c.itermonthdates(self.start_date.year, self.start_date.month))
        self._start_month_days = list(filter(lambda d: d >= self.start_date, start_month))

        expire_month = c.itermonthdates(self.expire_date.year, self.expire_date.month)
        self._expire_month_days = list(filter(lambda d: d <= self.expire_date, expire_month))

        self._days = self._start_month_days + self._expire_month_days

    def __repr__(self):
        return "{start_date: " + str(self.start_date) + ", expire_date: " + str(self.expire_date) + "}"

    @property
    def start_month_days(self):
        return self._start_month_days

    @property
    def expire_month_days(self):
        return self._expire_month_days

    @property
    def days(self):
        return self._days
