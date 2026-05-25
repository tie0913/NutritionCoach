from app.model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from exception import NutriCoachException


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def sign_up(self, data):
        existing_user = self.user_repository.find_by_email(
            data.get("email")
        )
        if existing_user:
            raise NutriCoachException(message="Email already exists")
        user = User(
            name=data.get("name"),
            password=generate_password_hash(
                data.get("password")
            ),
            email=data.get("email"),
            birth_date=datetime.strptime(
                data.get("birth_date"),
                "%Y-%m-%d"
            ).date()
        )

        return self.user_repository.save(user)

    def sign_in(self, data):

        email = data.get("email")
        password = data.get("password")

        user = self.user_repository \
            .find_by_email(email)

        if not user:
            raise NutriCoachException(message="Email and Password are not match")

        if not check_password_hash(
                user.password,
                password):
            raise NutriCoachException(message="Email and Password are not match")

        return user



    def get_current_user(self, user_id):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise NutriCoachException(message="User not found")
        return user

    def delete_account(self, user_id):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise NutriCoachException(message="User not found")
        self.user_repository.delete(user)
