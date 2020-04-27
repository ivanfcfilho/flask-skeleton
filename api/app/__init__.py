import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import InternalServerError, NotFound

from app.views.public.api import public_bp


def make_app():
    environment = os.environ.get("APPLICATION_ENV", "development")

    application = Flask(__name__)
    application.config.from_object("app.config.default")
    # application.config.from_object(f"config.{environment}")

    # TODO: CORS on production only from origin on AWS
    CORS(application)

    # You can create new APIs by adding them to the API folder, creating a blueprint and adding it here
    application.register_blueprint(public_bp)

    # Uncomment the line below to connect to the services' mongo database
    # mongodb.connect(application.config["MONGO_URL"])

    @application.before_request
    def log_requests():
        # TODO: Log
        pass

    @application.errorhandler(NotFound)
    def handle_404(_):
        return jsonify({"message": "The URL requested doesn't exist"}), 404

    @application.errorhandler(InternalServerError)
    def handle_500(_):
        return jsonify({"message": "Internal Server Error"}), 500

    return application


app = make_app()
