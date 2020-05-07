import os


from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


from app.views.public.api import public_bp


def make_app():
    environment = os.environ.get("APPLICATION_ENV", "local")

    application = Flask(__name__)
    application.config.from_object("config.default")
    application.config.from_object(f"config.{environment}")

    # TODO: CORS on production only from origin on AWS
    CORS(application)

    application.register_blueprint(public_bp)

    @application.before_request
    def log_requests():
        # TODO: Log
        pass

    @application.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code

    return application


app = make_app()


if __name__ == "__main__":
    app.run(debug=True)
