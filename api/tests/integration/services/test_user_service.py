import pytest
from werkzeug.exceptions import Conflict

from app.models.user import User
from app.services.user_service import UserService
from app.views.resources.user_resource import UserResource


@pytest.fixture
def user_fixture():
    # This fixture is to insert user in DB
    return User(email="ilovebeer@whiskye.tek", name="Jimi Page", password="letsdoit").save()


def test_email_already_exists(user_fixture):
    """
    Test if user exists already exists in the DB
    """

    # define expected message error
    expected_msg = "Email already in use."

    # set user data to be save
    user = {
        "email": user_fixture.email,
        "name": user_fixture.name,
        "password": user_fixture.password,
    }

    # call the function and test the exception
    with pytest.raises(Conflict) as excinfo:
        UserService.save(user)
        assert expected_msg == str(excinfo.value)


def test_success():
    """
    Test if data was inserted into DB
    """

    # set user data to be save
    email = "justdoit@dodo.new"
    user = {
        "email": email,
        "name": "Pele Zica",
        "password": "Brazil vai que vai",
    }

    # call function
    r_user = UserService.save(user)

    # test if data was inserted into database
    # Assert if there is only one
    query_set = User.objects.raw({"email": email})
    assert query_set.count() == 1

    # Test if data was inserted correctly
    i_user = query_set.first()
    i_user = UserResource().dump(i_user)
    r_user = UserResource().dump(r_user)

    assert i_user == r_user
