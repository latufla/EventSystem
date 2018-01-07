import collections


class DBWrapper:
    def __init__(self, db):
        self.db = db

    def add(self, obj):
        if obj is None:
            return

        if isinstance(obj, collections.Iterable):
            for o in obj:
                self.db.session.add(o)
        else:
            self.db.session.add(obj)

    def delete(self, obj):
        if obj is None:
            return

        if isinstance(obj, collections.Iterable):
            for o in obj:
                self.db.session.delete(o)
        else:
            self.db.session.delete(obj)

    def commit(self):
        self.db.session.commit()
