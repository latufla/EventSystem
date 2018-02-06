class UserData:
    def __init__(self, id: int, name: str, url: str, image: str = None):
        self.id = id
        self.name = name
        self.url = url
        self.image = image

        self.points = 0
