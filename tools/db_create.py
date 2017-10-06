from models.user import User
from models.event_result import EventResult
from models.event import Event
from models.invite import Invite

from initter import db
db.drop_all()
db.create_all()