from datetime import datetime
from calendar import calendar

from models.user import User
from models.pass_card import PassCard


class PassCardService:
    def __init__(self, db):
        self.db = db

    def createPassCard(self, user: User, months: int, events_count: int):
        card = PassCard(
            owner_id=user.id
        )
        card.start_date = datetime.utcnow()
        card.expire_date = self._addMonths(card.start_date, months)
        card.events_max_count = events_count

        self.db.add(card)
        self.db.commit()

    def _addMonths(self, to_date: datetime, months: int):
        month = to_date.month - 1 + months
        year = int(to_date.year + month / 12)
        month = month % 12 + 1
        day = min(to_date.day, calendar.monthrange(year, month)[1])
        return datetime(year, month, day)
