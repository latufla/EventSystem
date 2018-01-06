from typing import List


class Loc:
    def __call__(self, loc_key: str, *args):
        return self.all[loc_key]["en"].format(*args)

    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"
    MONTHS = [JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]

    PASS_CARD_CALENDAR_LABEL = "pass_card_calendar_label"
    LESSON_CALENDAR_LABEL = "lesson_calendar_label"
    TOURNAMENT_LABEL = "tournament_calendar_label"
    GAME_LABEL = "game_calendar_label"

    CALENDAR_CONTENT_MENU_TAB = "calendar_content_menu_tab"
    EVENT_LIST_CONTENT_MENU_TAB = "event_list_content_menu_tab"
    PASS_CARD_CONTENT_MENU_TAB = "pass_card_content_menu_tab"

    NOT_READY_EVENT_STATE = "not_ready_event_state"
    STARTED_EVENT_STATE = "started_event_state"
    FINISHED_EVENT_STATE = "finished_event_state"
    REWARDED_EVENT_STATE = "rewarded_event_state"

    EVENTS_HISTORY_YOU_PARTICIPATE_AT = "events_history_you_participate_at"
    EVENTS_HISTORY_PARTICIPATED_AT = "events_history_participated_at"
    EVENTS_HISTORY_TOOK_PLACE = "events_history_took_place"
    EVENTS_HISTORY_AND_REWARD = "events_history_and_reward"

    PROFILE_EVENTS_HISTORY = "profile_events_history"
    PROFILE_POINTS = "profile_points"
    PROFILE_NO_EVENTS_PARTICIPATED = "profile_no_events_participated"

    def __init__(self):
        self.all = {
            self.JANUARY: {
                "en": "January",
            },
            self.FEBRUARY: {
                "en": "February",
            },
            self.MARCH: {
                "en": "March",
            },
            self.APRIL: {
                "en": "April",
            },
            self.MAY: {
                "en": "May",
            },
            self.JUNE: {
                "en": "June",
            },
            self.JULY: {
                "en": "July",
            },
            self.AUGUST: {
                "en": "August",
            },
            self.SEPTEMBER: {
                "en": "September",
            },
            self.OCTOBER: {
                "en": "October",
            },
            self.NOVEMBER: {
                "en": "November",
            },
            self.DECEMBER: {
                "en": "December",
            },

            self.CALENDAR_CONTENT_MENU_TAB: {
                "en": "Calendar",
            },
            self.EVENT_LIST_CONTENT_MENU_TAB: {
                "en": "Events",
            },
            self.PASS_CARD_CONTENT_MENU_TAB: {
                "en": "Pass card",
            },

            self.PASS_CARD_CALENDAR_LABEL: {
                "en": "Calendar",
            },
            self.LESSON_CALENDAR_LABEL: {
                "en": "Lesson",
            },
            self.TOURNAMENT_LABEL: {
                "en": "Tournament",
            },
            self.GAME_LABEL: {
                "en": "Game",
            },

            self.NOT_READY_EVENT_STATE: {
                "en": "Not ready",
            },
            self.STARTED_EVENT_STATE: {
                "en": "Started",
            },
            self.FINISHED_EVENT_STATE: {
                "en": "Finished",
            },
            self.REWARDED_EVENT_STATE: {
                "en": "Rewarded",
            },

            self.EVENTS_HISTORY_PARTICIPATED_AT: {
                "en": "Participated at <a href='{0}'>{1}</a>",
            },
            self.EVENTS_HISTORY_YOU_PARTICIPATE_AT: {
                "en": "You participate at <a href='{0}'>{1}</a>",
            },
            self.EVENTS_HISTORY_TOOK_PLACE: {
                "en": "You took <strong>{0}</strong> place",
            },
            self.EVENTS_HISTORY_AND_REWARD: {
                "en": "and get <strong>{0}</strong> points",
            },

            self.PROFILE_EVENTS_HISTORY: {
                "en": "Events history",
            },
            self.PROFILE_POINTS: {
                "en": "{0} points",
            },
            self.PROFILE_NO_EVENTS_PARTICIPATED: {
                "en": "You`ve never participated in any events",
            }
        }
