from flask_restplus import Namespace

from app.decorators.check_body import check_body
from app.services.user_service import UserService
from app.views.resources.db_resource import DBResource
from app.views.resources.user_resource import UserResource

user_ns = Namespace("user")


@user_ns.route("/")
class UserEndpoint(DBResource):
    @check_body(UserResource)
    def post(self, data):
        user = UserService.save(data)
        return UserResource().dump(user)
