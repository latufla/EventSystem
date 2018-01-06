from view.data.event import Event


class View:
    def __init__(self, event: Event, creator: bool, add_participant_url: "", remove_participant_url: ""):
        self.event = event
        self.creator = creator

        self.add_participant_url = add_participant_url
        self.remove_participant_url = remove_participant_url

        self.min_width = 700
        self.max_width = 1200
