from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from services.media_service import get_image_path

app = Flask(__name__)
app.secret_key = "iodehjoiwjetsadfokiapserq"

# simple cloud host 85.143.173.86
app.config.from_pyfile("app.cfg")

db = SQLAlchemy(app)

app.jinja_env.globals.update(get_image_path=get_image_path)