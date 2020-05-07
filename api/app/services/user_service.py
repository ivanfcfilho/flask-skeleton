from app.models.user import User
from werkzeug.exceptions import Conflict


class UserService:

    @staticmethod
    def save(data):
        if User.objects.raw({"email": data["email"]}).count() > 0:
            raise Conflict("Email already in use.")

        return User(
            email=data["email"],
            name=data["name"],
            password=data["password"]
        ).save()
