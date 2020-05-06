import bcrypt
from bson import ObjectId
from marshmallow import fields


class ObjectIDField(fields.String):
    def _serialize(self, value, attr, obj, **kwargs):
        return str(value)

    def _deserialize(self, value, attr, data, **kwargs):
        return ObjectId(value)


class PwdException(Exception):
    # You never should return password in API
    pass


class PwdField(fields.String):
    def _serialize(self, value, attr, obj, **kwargs):
        import ipdb
        ipdb.set_trace()
        raise PwdException("Not allowed.")

    def _deserialize(self, value, attr, data, **kwargs):
        return str(bcrypt.hashpw(value.encode(), bcrypt.gensalt()))
