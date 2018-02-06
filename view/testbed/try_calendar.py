from datetime import datetime, timedelta
from jinja2 import Environment, PackageLoader, select_autoescape

from view.config import Config as ViewConfig
from view.data.event import EventData
from view.data.month import MonthData
from view.data.pass_card import PassCardData
from view.enum.event_label import EventLabels
from view.enum.event_state import EventStates
from view.loc import Loc
from view.view.calendar import CalendarView, Tabs

now = datetime.utcnow()

month = MonthData(now.date())

pass_card = PassCardData(now.date(), 31, 8)
month.apply_pass_card(pass_card)

event0 = EventData(0, "Game 1: Starters", datetime(2018, 1, 6), EventLabels.GAME, "http://google.com")
event0.description_short = "Very first game"
event0.state = EventStates.FINISHED
month.add_event(event0)
pass_card.events_visited.append(event0)

event = EventData(1, "Lesson 2: Red card", now + timedelta(days=2), EventLabels.LESSON, "http://ya.com")
event.description_short = "Being a good red citizen"
month.add_event(event)

event21 = EventData(2, "Lesson 3: Black card", now + timedelta(days=7), EventLabels.LESSON, "http://ok.ru")
event21.priority = 2
event21.description_short = "Being a good black citizen"
month.add_event(event21)

event2 = EventData(3, "Tournament: Straters", now + timedelta(days=7, hours=4), EventLabels.TOURNAMENT, "http://vk.com")
event2.priority = 1
event2.description_short = "First year novices are welcome"
month.add_event(event2)

view = CalendarView(month, pass_card, EventLabels.ALL, "http://google.com", "http://ya.com")
view.active_tab = Tabs.CALENDAR

env = Environment(
    loader=PackageLoader('PyTest', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('testbed/try_calendar.html')
html = template.render(view=view, config=ViewConfig(), loc=Loc())

with open("test_bed.html", "w") as file:
    file.write(html)


