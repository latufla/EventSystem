from datetime import datetime
from calendar import monthrange

from sqlalchemy import desc

from models.event import Event
from models.user import User
from models.pass_card import PassCard
from services.errors import ESError, PassCardErrors


class PassCardService:
    def __init__(self, db):
        self.db = db

    # CREATE PASS CARD
    def tryCreatePassCard(self, now: datetime,
                          user: User, months: int, events_count: int) -> ESError or PassCard:
        error = self.canCreatePassCard(now, user)
        if error:
            return error

        card = self._createPassCard(now, user, months, events_count)
        return card

    def canCreatePassCard(self, now: datetime, user: User) -> ESError or None:
        card = self._getPassCard(user)
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
    # END CREATE PASS CARD

    # USE PASS CARD
    def tryUsePassCard(self, now: datetime, user: User, event: Event) -> PassCard or ESError:
        card = self._getPassCard(user)
        if not card:
            return ESError(PassCardErrors.NEVER_BOUGHT, " id: " + str(card.id))

        error = self.canUsePassCard(now, card, event)
        if error:
            return error

        card = self._usePassCard(card, event)
        return card

    def canUsePassCard(self, now: datetime, card: PassCard, event:Event) -> ESError or None:
        if card.expire_date <= now:
            return ESError(PassCardErrors.EXPIRED, " id: " + str(card.id))

        events_count = card.events_visited.count()
        if events_count >= card.events_max_count:
            return ESError(PassCardErrors.EVENTS_EXCEEDED, " id: " + str(card.id))

        same_event = event in card.events_visited
        if same_event:
            return ESError(PassCardErrors.EVENT_ALREADY_USED, " event_id: " + str(event.id))

        return None

    def _usePassCard(self, card: PassCard, event: Event) -> PassCard:
        card.events_visited.append(event)
        return card
    # END USE PASS CARD

    def _getPassCard(self, user: User) -> PassCard:
        return user.pass_cards.order_by(desc("expire_date")).first()

    def _addMonths(self, to_date: datetime, months: int) -> datetime:
        month = to_date.month - 1 + months
        year = int(to_date.year + month / 12)
        month = month % 12 + 1
        day = min(to_date.day, monthrange(year, month)[1])
        return datetime(year, month, day)
