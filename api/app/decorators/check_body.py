from functools import wraps

from flask import request
from marshmallow import Schema
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest


def check_body(schema):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            application_json = "application/json"
            mult_form_data = "multipart/form-data"

            # Check for headers, only accept files and json
            content_type = request.content_type
            if not content_type or (
                content_type != application_json and mult_form_data not in content_type
            ):
                msg = f'Content-Type must be "{application_json}" or "{mult_form_data}"'
                raise BadRequest(msg)
            # Check if the data is a file ou a json
            if mult_form_data in content_type:
                r_json = {**request.files.to_dict(flat=False), **request.form.to_dict(flat=False)}
            else:
                try:
                    r_json = request.get_json()
                except BadRequest:
                    r_json = {}

            if r_json:
                # Use marshmellow validations
                serial = schema if isinstance(schema, Schema) else schema()
                try:
                    document = serial.load(r_json)
                    kwargs["data"] = document
                except ValidationError as e:
                    raise BadRequest(e.messages)
            else:
                raise BadRequest("Empty Json is not allowed.")

            return func(*args, **kwargs)

        return wrapper

    return real_decorator
