from EventSystem import db
from models.event import Event
from models.user import User
from models.event_result import EventResult

db.drop_all()
db.create_all()