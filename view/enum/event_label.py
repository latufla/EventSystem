from view.data.icon import Icon
from view.loc import Loc


class Label:
    def __init__(self, type_name: str, loc_key: str, color: str = None, icon: Icon = None):
        self.type_name = type_name

        self.loc_key = loc_key
        self.color = color

        self.icon = icon


class EventLabels:
    PASS_CARD = Label("PassCard", Loc.PASS_CARD_CALENDAR_LABEL, "#ADD8E6")
    LESSON = Label("Lesson", Loc.LESSON_CALENDAR_LABEL, "darkcyan", Icon("book icon", "white"))
    TOURNAMENT = Label("Tournament", Loc.TOURNAMENT_LABEL, "darkorange", Icon("trophy icon", "white"))
    GAME = Label("Game", Loc.GAME_LABEL, "darksalmon", Icon("game icon", "white"))

    EVENT_TYPES = [LESSON, TOURNAMENT, GAME]
    ALL = [PASS_CARD, LESSON, TOURNAMENT, GAME]