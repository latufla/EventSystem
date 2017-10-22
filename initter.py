from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "iodehjoiwjetsadfokiapserq"

# simple cloud host 85.143.173.86
app.config.from_pyfile("app.cfg")

db = SQLAlchemy(app)
