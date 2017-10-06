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


if __name__ == '__main__':
    app.run(debug=True)
