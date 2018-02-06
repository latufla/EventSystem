from datetime import datetime, timedelta

from jinja2 import Environment, PackageLoader, select_autoescape

from view.config import Config as ViewConfig
from view.data.event import EventData
from view.data.event_history_record import EventHistoryRecordData
from view.enum.event_label import EventLabels
from view.loc import Loc
from view.view.events_history import EventsHistoryView

now = datetime.utcnow()

events = [
    EventData(0, "Game 1: Starters", datetime(2018, 1, 6), EventLabels.GAME, "http://google.com"),
    EventData(1, "Lesson 2: Red card", now + timedelta(days=2), EventLabels.LESSON, "http://ya.com"),
    EventData(3, "Tournament: Starters", now + timedelta(days=7, hours=4), EventLabels.TOURNAMENT, "http://vk.com")
]

events_history = list(
    map(lambda e: EventHistoryRecordData(e, 1, 1000, True), events)
)

view = EventsHistoryView(events_history)

env = Environment(
    loader=PackageLoader('PyTest', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('testbed/try_events_history.html')
html = template.render(view=view, config=ViewConfig(), loc=Loc())

with open("test_bed.html", "w") as file:
    file.write(html)
