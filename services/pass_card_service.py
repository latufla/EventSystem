from datetime import datetime
from calendar import monthrange

from sqlalchemy import desc

from models.user import User
from models.pass_card import PassCard
from services.errors import ESError, PassCardErrors


class PassCardService:
    def __init__(self, db):
        self.db = db

    def tryCreatePassCard(self, now: datetime,
                          user: User, months: int, events_count: int) -> ESError or PassCard:
        error = self.canCreatePassCard(now, user)
        if error:
            return error

        card = self._createPassCard(now, user, months, events_count)
        return card

    def canCreatePassCard(self, now: datetime, user: User) -> ESError or None:
        card = user.pass_cards.order_by(desc("expire_date")).first()
        if card:
            if card.expire_date > now:
                return ESError(PassCardErrors.NOT_EXPIRED, " id: " + str(card.id))

        return None

    def _createPassCard(self, now: datetime, user: User, months: int, events_count: int) -> PassCard:
        card = PassCard(
            owner_id=user.id
        )
        card.start_date = now
        card.expire_date = self._addMonths(card.start_date, months)
        card.events_max_count = events_count

        return card

    @classmethod
    def _addMonths(cls, to_date: datetime, months: int) -> datetime:
        month = to_date.month - 1 + months
        year = int(to_date.year + month / 12)
        month = month % 12 + 1
        day = min(to_date.day, monthrange(year, month)[1])
        return datetime(year, month, day)
