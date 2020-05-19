from flask import current_app
from pymodm.connection import connect
from werkzeug.exceptions import BadRequest


class DBConnection:
    def __init__(self):
        with current_app.app_context():
            try:
                connect(current_app.config["MONGO_URL"])
            except Exception:
                raise BadRequest("Could not connecto to database.")
