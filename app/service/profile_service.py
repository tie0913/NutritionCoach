from datetime import date

from marshmallow import ValidationError

from app.model.profile import Profile
from app.model.user import User
from app.repository.profile_repo import ProfileRepository
from app.api.schema.profile_schema import profile_schema
from app.repository.user_repo import UserRepository


class ProfileService:

    @staticmethod
    def get_profile(user_id):
        return ProfileRepository.get_by_user_id(user_id)

    @staticmethod
    def save_profile(user_id, data):

        profile = ProfileRepository.get_by_user_id(user_id)
        age = ProfileService.get_user_age(user_id)

        if profile is None:
            profile = Profile(
                user_id=user_id,
                weight=data.get("weight"),
                height=data.get("height"),
                BMR= ProfileService.calculate_bmr(data.get("height"), data.get("weight"), age),
                chronic=data.get("chronic"),
                allergies=data.get("allergies"),
                goals=data.get("goals")
            )

            profile = ProfileRepository.create(profile)

        else:
            data["BMR"] = ProfileService.calculate_bmr(data.get("height"), data.get("weight"), age),
            profile = ProfileRepository.update(profile, data)

        return profile_schema.dump(profile)

    @staticmethod
    def get_user_age(user_id):
        user = UserRepository.find_by_id(user_id)
        birth_date = user.birth_date
        today = date.today()

        return (
                today.year
                - birth_date.year
                - (
                        (today.month, today.day)
                        < (birth_date.month, birth_date.day)
                )
        )

    @staticmethod
    def calculate_bmr(height, weight, age):
        return int(
            10 * weight
            + 6.25 * (height * 100)
            - 5 * age
            + 5
        )