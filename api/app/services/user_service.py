from pymongo.errors import ServerSelectionTimeoutError
from werkzeug.exceptions import Conflict

from app.models.user import User
from app.repository.db_connection import DBConnection


class UserService(DBConnection):
    def save(self, data: dict) -> User:
        try:
            if User.objects.raw({"email": data["email"]}).count() > 0:
                raise Conflict("Email already in use.")

            return User(email=data["email"], name=data["name"], password=data["password"]).save()
        except ServerSelectionTimeoutError as err:
            raise ServerSelectionTimeoutError(f"DataBasse connection error: {str(err)}")
