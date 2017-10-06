from models.user import User
from models.event_result import EventResult
from models.event import Event
from models.invite import Invite

import router
router.db.drop_all()
router.db.create_all()