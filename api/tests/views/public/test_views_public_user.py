import pytest
from app.models.user_model import UserModel


@pytest.fixture
def user_fixture():
    # This fixture is to insert user in DB
    return UserModel(
        email="ilovebeer@whiskye.tek",
        name="Jimi Page",
        password="letsdoit"
    ).save()


def test_post_name_missing(tst):
    # Test if the name field is mandatory
    # If dont, returns 400 status code and a json error message

    # Define the body requisition
    user = {
        "user_email": "aa@clinic.com",
        "user_pwd": "aa123"
    }

    # Define expecting response
    expected_status_code = 400
    expected_json_body = {
        "message": {
            "name": [
                "Missing data for required field."
            ]
        }
    }

    # Call /user/ endpoint
    ret = tst.client.post("/user/")

    # assert response
    assert ret.status_code == expected_status_code
    assert ret.json() == expected_json_body


def test_post_email_missing(tst, user_fixture):
    assert False


def test_post_password_missing(tst, user_fixture):
    assert False


def test_post_email_already_exists(tst, user_fixture):
    assert False


def test_post_success(tst, user_fixture):
    assert False


def test_post_pwd_encrypt(tst, user_fixture):
    assert False


def tst_post_success_excessive_fields(tst, user_fixture):
    assert False
