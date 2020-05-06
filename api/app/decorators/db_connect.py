from functools import wraps

from flask import current_app, request
from marshmallow import Schema
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest
from pymodm.connection import connect


def db_connect(schema):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            with current_app.app_context():
                # Connect to MongoDB and call the connection "my-app".
                connect(current_app.config["MONGO_URL"])

            return func(*args, **kwargs)

        return wrapper

    return real_decorator
