from openpyxl import load_workbook

from models.event_result import EventResult
from models.user import User

from initter import db


class RewardService:

    def collectResults(self, event):
        wb = load_workbook(event.result_file)
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
                db.session.add(user)

            event.results.append(res)
            user.events_history.append(res)

        wb.close()

    def giveRewards(self, event):
        pass
        # not_rewarded_results = [r for r in event.results if not r.rewarded]
        # for r in not_rewarded_results:
        #     u = User.objects(login=r.user_name).first()
        #     if u is not None:
        #         u.xp += r.reward
        #
        #         event_record = next((e for e in u.events_history if e.event_id == event.id), None)
        #         if event_record is None:
        #             u.events_history.append(EventHistoryRecord(
        #                 event_id= event.id,
        #                 title=event.title,
        #                 place=None,
        #                 reward=r.reward,
        #                 date_start=event.date_start
        #             ))
        #
        #         u.save()
        #
        #         r.rewarded = True
