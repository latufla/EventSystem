import os
from openpyxl import load_workbook

from models.event_result import EventResult
from models.unregistered_password import UnregisteredPassword
from models.user import User


class RewardService:
    def __init__(self, db, app):
        self.db = db
        self.app = app

    def collectResults(self, event, password_generator):
        path = os.path.join(self.app.root_path, event.result_file)
        wb = load_workbook(path)
        sheet = wb.get_sheet_by_name('Sheet1')
        for row in sheet.rows:
            res = EventResult(
                place=row[1].value,
                reward=row[2].value,
                rewarded=False
            )

            login = row[0].value
            user = User.query.filter_by(login=login).first()
            if user is None:
                user = User(login=login)
                password = UnregisteredPassword(password=password_generator.generate(10))
                user.unregistered_password = password
                self.db.add(user)

            event.results.append(res)
            user.events_history.append(res)

        wb.close()

    def giveRewards(self, event):
        not_rewarded_results = event.results.filter_by(rewarded=False)
        for result in not_rewarded_results:
            result.user.xp += result.reward
            result.rewarded = True
