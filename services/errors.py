from enums.enums import EnumBase


class PassCardErrors(EnumBase):
    NOT_EXPIRED = "pass_card_not_expired"


class ESError:
    def __init__(self, code, message):
        self.code = code
        self.message = message
