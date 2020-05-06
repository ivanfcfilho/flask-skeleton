from pymodm import fields, MongoModel


class UserModel(MongoModel):
    # Use 'email' as the '_id' field in MongoDB.
    email = fields.EmailField()
    name = fields.CharField()
    password = fields.CharField()
