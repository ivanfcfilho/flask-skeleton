from flask import current_app, request
from flask_restplus import Namespace, Resource
from pymodm.connection import connect
from werkzeug.exceptions import BadRequest


class DBResource(Resource):
    def __init__(self, _):
        with current_app.app_context():
            try:
                connect(current_app.config["MONGO_URL"])
            except Exception:
                raise BadRequest("Could not connecto to database.")
