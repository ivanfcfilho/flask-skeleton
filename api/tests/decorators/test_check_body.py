
import json

import pytest
from werkzeug.exceptions import BadRequest

from app.decorators.check_body import check_body
from app.views.resources.user_resource import UserResource


def test_check_body_wrong_content_type(tst, mocker):
    """
    Test for invalid content-type header.
    First test for None, then test for invalid one.
    """

    l_content_type = [None, "text/html"]
    for content_type in l_content_type:
        with tst.context:
            # mock flask request content_type
            mocker.patch("app.decorators.check_body.request", content_type=content_type)

            # define call check_body to call on function
            @check_body(UserResource)
            def test_func():
                return

            # define message should be returned from decorator
            expected_msg = 'Content-Type must be "application/json" or "multipart/form-data"'
            with pytest.raises(BadRequest) as excinfo:
                # call function to test decorator
                test_func()

            # assert expected message
            assert expected_msg == str(excinfo.value).split(":")[1].strip()


def test_check_body_empty_json(tst, mocker):
    """
    Test if json is not empty.
    """
    with tst.context:
        # mock flask request content_type
        # mock flask request content_type
        mocker.patch(
            "app.decorators.check_body.request",
            content_type="application/json",
            get_json=lambda: {},
        )

        # define call check_body to call on function
        @check_body(UserResource)
        def test_func():
            return

        # define message should be returned from decorator
        expected_msg = "Empty Json is not allowed."
        with pytest.raises(BadRequest) as excinfo:
            # call function to test decorator
            test_func()

        # assert expected message
        assert expected_msg == str(excinfo.value).split(":")[1].strip()


def test_check_body_invalid_schema(tst, mocker):
    """
    Test for invalid payload json.
    Application must throw marshmallow exception.
    """
    with tst.context:
        # mock flask request content_type
        # will send a payload with missing args
        mocker.patch(
            "app.decorators.check_body.request",
            content_type="application/json",
            get_json=lambda: {"phone": "19991455685"},
        )

        # define call check_body to call on function
        @check_body(UserResource)
        def test_func():
            return

        # define message should be returned from decorator
        expected_msg = {"email": ["Missing data for required field."],
                        "password": ["Missing data for required field."],
                        "name": ["Missing data for required field."],
                        "phone": ["Unknown field."]}

        with pytest.raises(BadRequest) as excinfo:
            # call function to test decorator
            test_func()

        # assert expected message

        assert expected_msg == json.loads(str(excinfo.value).split("Request:")[1:][0].replace("'", '"'))


def test_check_body_valid_schema(tst, mocker):
    """
    Json will be send and everything must work as expected.
    data will be returned as argument of test_func
    """
    with tst.context:

        # define user to be send
        user = {"name": "name", "email": "email@email.com", "password": "xablau"}

        # mock things
        mocker.patch(
            "app.decorators.check_body.request",
            content_type="application/json",
            get_json=lambda: user,
        )

        # define call check_body to call on function
        @check_body(UserResource)
        def test_func(data):
            return data

        # define message should be returned from decorator
        expected_msg = ""

        # execute function and get the decorator return
        data = test_func()

        # assert exepcted data
        assert data["email"] == user["email"]
        assert data["name"] == user["name"]
        # password must be encrypt so it will be different
        assert data["password"] and data["password"] != user["password"]


def test_check_body_multform_empty():
    """
    Payload with multform data is empty
    """
    # TODO
    pass


def test_check_body_multform_success():
    """
    Payload with multform data is not empty and its correct
    Everything is fine
    """
    # TODO
    pass
