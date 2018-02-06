from datetime import datetime, timedelta

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

from view.config import Config as ViewConfig
from view.data.userdata import UserData
from view.enum.event_state import EventStates
from view.loc import Loc
from view.view.profile import ProfileView

from view.data.event import EventData
from view.data.event_history_record import EventHistoryRecordData
from view.enum.event_label import EventLabels

now = datetime.utcnow()

user = UserData(1, "Red Fox", "", "https://pbs.twimg.com/profile_images/606791373593837568/eL5DHK0L.png")
user.points = 1000

e = EventData(0, "Game 1: Starters", datetime(2018, 1, 6), EventLabels.GAME, "http://google.com")
e.state = EventStates.REWARDED
e.participant_list.append(user)

# you were only waiter, so it`s gonna
e2 = EventData(1, "Lesson 2: Red card", now + timedelta(days=2), EventLabels.LESSON, "http://ya.com")
e2.state = EventStates.FINISHED
e2.wait_list.append(user)

e3 = EventData(2, "Tournament: Starters", now + timedelta(days=7, hours=4), EventLabels.TOURNAMENT, "http://vk.com")
e3.state = EventStates.REWARDED
e3.participant_list.append(user)

e4 = EventData(3, "Tournament 2: Starters", now + timedelta(days=9, hours=4), EventLabels.TOURNAMENT, "http://vk.com")
e4.state = EventStates.STARTED
e4.wait_list.append(user)

e5 = EventData(3, "Tournament 3: Starters", now + timedelta(days=10, hours=4), EventLabels.TOURNAMENT, "http://vk.com")
e5.state = EventStates.STARTED
e5.participant_list.append(user)

events_history = [
    EventHistoryRecordData(e, 1, 1000, True),
    EventHistoryRecordData(e2),
    EventHistoryRecordData(e3, 2, 500),
    EventHistoryRecordData(e4),
    EventHistoryRecordData(e5)
]

view = ProfileView(user, events_history, False, True, "")
view.order_history()

env = Environment(
    loader=FileSystemLoader('../../templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('testbed/try_profile.html')
html = template.render(view=view, config=ViewConfig(), loc=Loc("en"))

with open("test_bed.html", "w") as file:
    file.write(html)
