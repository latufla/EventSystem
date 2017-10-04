from enum import Enum


class EnumBase(Enum):
    @classmethod
    def HasName(cls, name):
        names = [item.name for item in cls]
        return name in names


class UserRole(EnumBase):
    ADMIN = 1,
    USER = 2


class EventStatus(EnumBase):
    NOT_READY = 1
    STARTED = 2
    FINISHED = 3
    REWARDED = 4


class Gender(EnumBase):
    MALE = 1,
    FEMALE = 2