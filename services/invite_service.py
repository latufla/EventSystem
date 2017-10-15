import random

from models.invite import Invite


class InviteService:
    __alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, db):
        self.db = db

    def hasInvite(self, key):
        inv = Invite.query.filter_by(key=key).first()
        return inv is not None

    def tryUseInvite(self, key):
        inv = Invite.query.filter_by(key=key).first()
        if inv is None:
            return False

        self.db.delete(inv)
        self.db.commit()

        return True

    def createInvites(self, count, length):
        invites = self.__generator(count, length)
        for i in invites:
            inv = Invite(key=i)
            self.db.add(inv)

        self.db.commit()

    def getInvites(self):
        invites = Invite.query.all()
        if invites is None:
            return []

        return [item.key for item in invites]

    def generate(self, length):
        return self.__generator(1, length)[0]

    @classmethod
    def __generator(cls, count, length):
        invites = []

        n = len(cls.__alphabet)

        for i in range(count):

            inv = ""
            for j in range(length):
                next_index = random.randrange(n)
                inv += cls.__alphabet[next_index]

            invites.append(inv)

        return invites
