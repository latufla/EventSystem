from flask import request, render_template

from initter import *

from controller import Controller
# from services.UserService import is_not_logged_in

ctr = Controller(app, db)


@app.route('/register', methods=['GET', 'POST'])
# @is_not_logged_in
def register():
    if request.method == 'POST':
        return ctr.registerUser()

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
