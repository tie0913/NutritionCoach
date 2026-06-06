from app.model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app.repository.user_repo import UserRepository
from exception import NutriCoachException


class UserService:

    @staticmethod
    def sign_up(data):
        existing_user = UserRepository.find_by_email(
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
            birth_date=data.get("birth_date")
        )

        return UserRepository.save(user)

    @staticmethod
    def sign_in(data):

        email = data.get("email")
        password = data.get("password")

        user = UserRepository \
            .find_by_email(email)

        if not user:
            raise NutriCoachException(message="Email and Password are not match")

        if not check_password_hash(
                user.password,
                password):
            raise NutriCoachException(message="Email and Password are not match")

        return user



    @staticmethod
    def get_current_user(user_id):
        user = UserRepository.find_by_id(user_id)
        if not user:
            raise NutriCoachException(message="User not found")
        return user

    @staticmethod
    def delete_account(user_id):
        user = UserRepository.find_by_id(user_id)
        if not user:
            raise NutriCoachException(message="User not found")
        UserRepository.delete(user)
