import datetime


class DayData:
    """
    Day with possible event
    """

    def __init__(self, date: datetime.date):
        self.date = date
        self.events = []

        self.label = None

    def __repr__(self):
        return "{date: " + str(self.date) + ", event: " + str(self.events) + "}"

    def get_color(self):
        if len(self.events) > 0:
            events_by_priority = sorted(self.events, key=lambda e: e.priority)
            return events_by_priority[0].label.color

        if self.label:
            return self.label.color

        return None

    def get_event_icons(self):
        return list(map(lambda e: e.label.icon, self.events))
