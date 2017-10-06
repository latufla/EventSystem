from flask import request, render_template

from initter import *

from controller import Controller
from services.UserService import *

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
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

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


if __name__ == '__main__':
    app.run(debug=True)
