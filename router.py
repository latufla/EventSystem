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


if __name__ == '__main__':
    app.run(debug=True)
