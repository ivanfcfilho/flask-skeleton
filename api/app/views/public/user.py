from app.decorators.check_body import check_body
from app.http_responses.http_responses import conflict
from app.models.user_model import UserModel
from app.schemas.user_schema import UserSchema
from app.views.db_api import DBApi
from flask import current_app
from flask_restplus import Namespace, Resource
from pymodm.connection import connect

user_ns = Namespace("user")


@user_ns.route("/")
class UserEndpoint(DBApi):
    @check_body(UserSchema)
    def post(self, data):

        if UserModel.objects.raw({"email": data["email"]}).count() > 0:
            return conflict("Email already in use.")

        user = UserModel(
            email=data["email"],
            name=data["name"],
            password=data["password"]
        ).save()

        return UserSchema().dump(user)
