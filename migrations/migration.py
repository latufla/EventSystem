from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import sys

sys.path.append("../")

# add db models here
from models.user import User
from models.event_result import EventResult
from models.event import Event
from models.invite import Invite
from models.unregistered_password import UnregisteredPassword
# --

from initter import db, app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
