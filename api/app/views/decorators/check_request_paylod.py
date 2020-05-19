from functools import wraps

from flask import request
from marshmallow import Schema
from marshmallow.exceptions import MarshmallowError
from werkzeug.exceptions import BadRequest


def check_request_paylod(schema):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            application_json = "application/json"

            # Check for headers, only accept json
            content_type = request.content_type
            if content_type != application_json:
                msg = f'Content-Type must be "{application_json}"'
                raise BadRequest(msg)
            try:
                r_json = request.get_json()
                serial = schema if isinstance(schema, Schema) else schema()
                kwargs["data"] = serial.load(r_json)
            except BadRequest as err:
                raise BadRequest(f"Error loading json data: {str(err)}")
            except MarshmallowError as err:
                raise BadRequest(f"Error validating json: {str(err)}")

            return func(*args, **kwargs)

        return wrapper

    return real_decorator
