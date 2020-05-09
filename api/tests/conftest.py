import os

import pymodm.connection as connection
import pytest
from pymodm.connection import connect
from pymongo import MongoClient

from run import make_app


@pytest.fixture(autouse=True, scope="session")
def session(worker_id):
    yield type("", (), {"worker_id": worker_id})


@pytest.fixture(autouse=True)
def tst(session):
    os.environ["APPLICATION_ENV"] = "testing"
    application = make_app()
    session.client = application.test_client()
    session.context = application.test_request_context()
    with application.app_context():
        connection.connect(application.config["MONGO_URL"])
        yield session
    client = connection._get_connection().database.client
    client.drop_database(application.config["MONGO_DB"])
