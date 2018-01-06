from datetime import datetime, timedelta

from jinja2 import Environment, PackageLoader, select_autoescape

from view.config import Config as ViewConfig
from view.data.event import Event as EventData
from view.enum.event_label import EventLabels
from view.loc import Loc
from view.view.event_edit import View

now = datetime.utcnow()

e = EventData(2, "Lesson 2: Red card", now + timedelta(days=2), EventLabels.TOURNAMENT, "http://ya.com")
e.description_short = "Being a good red citizen"

view = View(e, "", EventLabels.EVENT_TYPES)

env = Environment(
    loader=PackageLoader('PyTest', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('testbed/try_event_edit.html')
html = template.render(view=view, config=ViewConfig(), loc=Loc())

with open("test_bed.html", "w") as file:
    file.write(html)