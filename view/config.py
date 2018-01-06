from flask import url_for


class Config:
    def __init__(self, has_app_context=False):
        if has_app_context:

            self.semantic_ui = url_for('static', filename="node_modules/semantic-ui/semantic.min.js")
            self.semantic_ui_css = url_for('static', filename="node_modules/semantic-ui/semantic.min.css")

            self.jquery = url_for('static', filename="node_modules/jquery/jquery-3.2.1.min.js")

            self.semantic_ui_calendar = url_for('static', filename="node_modules/semantic-ui-calendar/dist/calendar.min.js")
            self.semantic_ui_calendar_css = url_for('static', filename="node_modules/semantic-ui-calendar/dist/calendar.min.css")

            self.ckeditor = url_for('static', filename="node_modules/ckeditor/ckeditor.js")

        else:

            self.semantic_ui = "../../static/node_modules/semantic-ui/semantic.min.js"
            self.semantic_ui_css = "../../static/node_modules/semantic-ui/semantic.min.css"

            self.jquery = "../../static/node_modules/jquery/jquery-3.2.1.min.js"

            self.semantic_ui_calendar = "../../static/node_modules/semantic-ui-calendar/dist/calendar.min.js"
            self.semantic_ui_calendar_css = "../../static/node_modules/semantic-ui-calendar/dist/calendar.min.css"

            self.ckeditor = "../../static/node_modules/ckeditor/ckeditor.js"
