import unittest

from flask_sqlalchemy import SQLAlchemy

import initter

initter.app.config.from_pyfile("test/test_app.cfg")
initter.db = SQLAlchemy(initter.app)

# add db models here
from models.user import User
from models.event_result import EventResult
from models.event import Event
from models.invite import Invite
from models.unregistered_password import UnregisteredPassword
# --

class TestBase(unittest.TestCase):
    def setUp(self):
        initter.db.create_all()

    def tearDown(self):
        initter.db.drop_all()

