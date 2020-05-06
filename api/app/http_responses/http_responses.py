from flask import abort, jsonify, make_response


def nocontent(message="no content.", **kwargs):
    abort(make_response(jsonify(message=message, **kwargs), 204))


def badrequest(message="bad request.", **kwargs):
    abort(make_response(jsonify(message=message, **kwargs), 400))


def unauthorized(message="unauthorized.", **kwargs):
    abort(make_response(jsonify(message=message, **kwargs), 401))


def forbidden(message="forbidden.", **kwargs):
    abort(make_response(jsonify(message=message, **kwargs), 403))


def notfound(message="not found.", **kwargs):
    abort(make_response(jsonify(message=message, **kwargs), 404))


def conflict(message="conflict.", **kwargs):
    abort(make_response(jsonify(message=message, **kwargs), 409))
