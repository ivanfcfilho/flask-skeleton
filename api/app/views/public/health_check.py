from flask_restplus import Namespace, Resource

health_check_ns = Namespace("health_check")


@health_check_ns.route("/")
class HealthCheck(Resource):
    def get(self):
        return {"message": "Hello World"}
