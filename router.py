from flask import request, render_template

from initter import *

from controller import Controller
from services.user_service import *

controller = Controller(app, db)


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


@app.route('/logout', methods=['GET'])
@is_logged_in
def logout():
    return controller.logoutUser()


@app.route('/', methods=['GET'])
@is_logged_in
def index():
    return redirect(url_for('profile'))


@app.route('/profile', methods=['GET'])
@is_logged_in
def profile():
    return controller.getUserProfile()


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


@app.route('/upload_avatar', methods=['POST'])
@is_logged_in
def upload_avatar():
    return controller.uploadAvatar()


@app.route('/upload_event_avatar/<int:event_id>', methods=['POST'])
@is_logged_in
def upload_event_avatar(event_id):
    return controller.uploadEventAvatar(event_id)


if __name__ == '__main__':
    app.run(debug=True)
