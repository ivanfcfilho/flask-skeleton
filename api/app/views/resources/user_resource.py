from app.views.resources.custom_fields import ObjectIDField, PwdField
from marshmallow import Schema, fields


class UserResource(Schema):
    _id = ObjectIDField()
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = PwdField(required=True, load_only=True)
