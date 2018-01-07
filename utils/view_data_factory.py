from typing import List

from flask import url_for

from enums.enums import EventStatus
from models.event import Event
from models.event_result import EventResult
from models.user import User
from services.media_service import get_image_path

from view.data.event_result import EventHistoryRecord as EventHistoryRecordData
from view.data.user import User as UserData
from view.data.event import Event as EventData
from view.enum.event_label import EventLabels
from view.enum.event_state import EventStates

event_status_to_state = {
    EventStatus.NOT_READY.name: EventStates.NOT_READY,
    EventStatus.STARTED.name: EventStates.STARTED,
    EventStatus.FINISHED.name: EventStates.FINISHED,
    EventStatus.REWARDED.name: EventStates.REWARDED
}


class UserDataCreator:
    @staticmethod
    def create(user: User):
        return UserData(
            user.id,
            user.login,
            url_for("profile", user_name=user.login),
            get_image_path(user.image_big)
        )


class EventHistoryRecordDataCreator:
    @staticmethod
    def create(event: Event) -> EventHistoryRecordData:
        event_data = EventData(event.id, event.title, event.date_start, EventLabels.GAME,
                               url_for('event', event_id=event.id))
        event_data.state = event_status_to_state[event.status]
        return EventHistoryRecordData(event_data)

    @staticmethod
    def create_list(events: List[Event]) -> List[EventHistoryRecordData]:
        res = []
        for e in events:
            res.append(EventHistoryRecordDataCreator.create(e))

        return res

    @staticmethod
    def apply_result(to_data: EventHistoryRecordData, result: EventResult) -> bool:
        if result.event.id == to_data.event.id:
            to_data.place = result.place
            to_data.reward = result.reward
            to_data.rewarded = result.rewarded
            return True

        return False

    @staticmethod
    def apply_result_list(to_data_list: List[EventHistoryRecordData], results: List[EventResult]):
        for d in to_data_list:
            for r in results:
                if EventHistoryRecordDataCreator.apply_result(d, r):
                    break
