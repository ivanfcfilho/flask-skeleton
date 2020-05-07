from pymodm import MongoModel, fields


class User(MongoModel):
    email = fields.EmailField()
    name = fields.CharField()
    password = fields.CharField()
