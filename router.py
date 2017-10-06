from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import controller
from services.UserService import *

app = Flask(__name__)
app.secret_key = "iodehjoiwjetsadfokiapserq"

app.config.from_pyfile("app.cfg")

db = SQLAlchemy(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return controller.registerUser(db)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
