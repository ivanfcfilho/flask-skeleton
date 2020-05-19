from flask_restplus import Namespace, Resource

from app.services.user_service import UserService
from app.views.decorators.check_request_paylod import check_request_paylod
from app.views.resources.user_resource import UserResource

user_ns = Namespace("user")


@user_ns.route("/")
class UserEndpoint(Resource):
    @check_request_paylod(UserResource)
    def post(self, data):
        user = UserService().save(data)
        return UserResource().dump(user)
