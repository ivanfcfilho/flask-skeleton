from flask_restplus import Api
from flask import Blueprint

from app.views.public.health_check import health_check_ns

public_bp = Blueprint("public_api", __name__)

api = Api(public_bp, decorators=[])

api.add_namespace(health_check_ns)
