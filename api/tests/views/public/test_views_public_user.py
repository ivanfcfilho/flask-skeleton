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


def test_post_name_missing(tst, user_fixture):
    assert False


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
