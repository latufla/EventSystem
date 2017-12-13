from enums.enums import EnumBase


class PassCardErrors(EnumBase):
    NOT_EXPIRED = "pass_card_not_expired",

    NEVER_BOUGHT = "pass_card_never_bought",
    EXPIRED = "pass_card_expired",
    EVENTS_EXCEEDED = "pass_card_events_exceeded"
    EVENT_ALREADY_USED = "pass_card_event_already_used"


class ESError:
    def __init__(self, code, message):
        self.code = code
        self.message = message
