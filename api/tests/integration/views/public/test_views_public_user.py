import copy
import json

import bcrypt
import pytest
from bson import ObjectId

from app.models.user import User


@pytest.fixture
def user_fixture():
    """
    This fixture is to insert user in DB
    """

    return User(email="ilovebeer@whiskye.tek", name="Jimi Page", password="letsdoit").save()


def test_post_fields_missing(tst):
    """
    Test for mandatory fields.
    If dont, returns 400 status code and a json error message
    """

    # Define the body requisition with all required fields
    user = {"name": "Marquito", "email": "marquitozica@germany.ik", "password": "marquitoZica"}

    for field, _ in user.items():
        # Iterate over all fields and remove each one to test all missing
        c_user = copy.deepcopy(user)
        del c_user[field]

        # Define expecting response
        expected_status_code = 400
        expected_json_body = {"message": {field: [f"Missing data for required field."]}}

        # Call /user/ endpoint
        headers = {"Content-Type": "application/json"}
        ret = tst.client.post("/user/", data=json.dumps(c_user), headers=headers)

        # assert response
        assert ret.status_code == expected_status_code
        assert ret.json == expected_json_body


def test_success(tst, mocker):
    """
    Teste the success return of API
    """

    # set user to be mocked
    name = "Alana Dias"
    email = "sexonfire@music.good"
    password = "pwseasybusy"
    _id = str(ObjectId())
    user = User(name=name, email=email, password=password, _id=_id)

    # mock user_service call
    mocker.patch("app.views.public.user.UserService.save", return_value=user)

    # set request headers
    headers = {"Content-Type": "application/json"}

    # set body
    body = {"name": name, "email": email, "password": password}

    # do request
    response = tst.client.post("/user/", headers=headers, data=json.dumps(body))

    # assert responses
    body["_id"] = _id
    del body["password"]
    assert response.status_code == 200
    assert response.json == body
