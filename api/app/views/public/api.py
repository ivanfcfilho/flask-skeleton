from flask import Blueprint
from flask_restplus import Api

from app.views.public.health_check import health_check_ns
from app.views.public.user import user_ns

public_bp = Blueprint("public_api", __name__)

api = Api(public_bp, decorators=[])

api.add_namespace(health_check_ns)
api.add_namespace(user_ns)
