from flask_restplus import Namespace, Resource
from flask import current_app, request
from pymodm.connection import connect

from app.schemas.user_schema import UserSchema


class DBApi(Resource):
    def __init__(self, _):
        with current_app.app_context():
            try:
                connect(current_app.config["MONGO_URL"])
            except Exception as e:
                # TODO: What is the best way to handle ? Which message ?
                pass
