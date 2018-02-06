from flask import request, render_template, send_file

from initter import *

from controller import Controller
from services.user_service import *

import json
import requests

controller = Controller(app, db)


@app.route('/register_invite', methods=['GET', 'POST'])
@is_not_logged_in
def register_invite():
    return controller.registerInvite()


@app.route('/register', methods=['GET', 'POST'])
@is_not_logged_in
def register():
    if request.method == 'POST':
        return controller.registerUser()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
@is_not_logged_in
def login():
    if request.method == 'POST':
        return controller.loginUser()

    return render_template('login.html')


@app.route('/social_enter', methods=['POST'])
@is_not_logged_in
def social_enter():
    token = request.form["token"]
    response = requests.get('http://ulogin.ru/token.php?token=' + token)
    user = json.loads(str(response.text))
    first_name = user["first_name"]
    last_name = user["last_name"]
    uid = user["uid"]

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
@is_logged_in
def logout():
    return controller.logoutUser()


@app.route('/', methods=['GET'])
@is_logged_in
def index():
    return controller.getIndex()


@app.route('/<string:user_name>', methods=['GET'])
@is_logged_in
def profile(user_name):
    return controller.get_user_profile(user_name)


@app.route('/all', methods=['GET'])
@is_logged_in
@is_admin
def all_users():
    return controller.getAllUsers()


@app.route('/events', methods=['GET'])
@is_logged_in
def events():
    return redirect(url_for('events_created'))


@app.route('/events_created', methods=['GET'])
@is_logged_in
@is_admin
def events_created():
    return controller.getCreatedEvents()


@app.route('/events_participate', methods=['GET'])
@is_logged_in
def events_participate():
    return controller.getParticipateEvents()


@app.route('/events_published', methods=['GET'])
@is_logged_in
def events_published():
    return controller.getPublishedEvents()


@app.route('/invites', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def invites():
    return controller.getInvites()


@app.route('/event_create', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def event_create():
    return controller.createEvent()


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def edit_event(event_id):
    return controller.editEvent(event_id)


@app.route('/delete_event', methods=['POST'])
@is_logged_in
@is_admin
def delete_event():
    return controller.deleteEvent()


@app.route('/event/<int:event_id>')
@is_logged_in
def event(event_id):
    return controller.getEvent(event_id)


@app.route('/participate_event/<int:event_id>', methods=['POST'])
@is_logged_in
def participate_event(event_id):
    return controller.participateEvent(event_id)


@app.route('/leave_event/<int:event_id>', methods=['POST'])
@is_logged_in
def leave_event(event_id):
    return controller.leaveEvent(event_id)


@app.route('/publish_event/<int:event_id>', methods=['POST'])
@is_logged_in
def publish_event(event_id):
    return controller.publishEvent(event_id)


@app.route('/unpublish_event/<int:event_id>', methods=['POST'])
@is_logged_in
def unpublish_event(event_id):
    return controller.unpublishEvent(event_id)


@app.route('/event_state_change', methods=['POST'])
@is_logged_in
@is_admin
def event_state_change():
    return controller.changeEventState()


@app.route('/event_add_participant', methods=['POST'])
@is_logged_in
@is_admin
def event_add_participant():
    return controller.addParticipantToEvent()


@app.route('/event_remove_participant', methods=['POST'])
@is_logged_in
@is_admin
def event_remove_participant():
    return controller.removeParticipantFromEvent()


@app.route('/upload_avatar', methods=['POST'])
@is_logged_in
def upload_avatar():
    return controller.uploadAvatar()


@app.route('/upload_event_avatar/<int:event_id>', methods=['POST'])
@is_logged_in
def upload_event_avatar(event_id):
    return controller.uploadEventAvatar(event_id)


@app.route('/settings', methods=['GET', 'POST'])
@is_logged_in
def settings():
    return controller.getSettings()


@app.route("/" + app.config['UPLOAD_FOLDER'] + "/" + "<path:filename>", methods=['GET'])
@is_logged_in
def uploads(filename):
    return send_file(app.config['UPLOAD_FOLDER'] + "/" + filename)


@app.route('/create_pass_card', methods=['POST'])
@is_logged_in
@is_admin
def create_pass_card():
    return controller.createPassCard()


@app.route('/use_pass_card', methods=['POST'])
@is_logged_in
def use_pass_card():
    return controller.usePassCard()


if __name__ == '__main__':
    app.run(debug=True)
    # app.run("0.0.0.0", port=8000)
