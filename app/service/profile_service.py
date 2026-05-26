from datetime import date

from marshmallow import ValidationError

from app.model.profile import Profile
from app.model.user import User
from app.repository.profile_repo import ProfileRepository
from app.api.schema.profile_schema import profile_schema


class ProfileService:

    def __init__(self, profile_repo, user_repo):
        self.profile_repo = profile_repo
        self.user_repo = user_repo

    def get_profile(self, user_id):
        return self.profile_repo.get_by_user_id(user_id)

    def save_profile(self, user_id, data):

        profile = self.profile_repo.get_by_user_id(user_id)
        age = self.get_user_age(user_id)

        if profile is None:
            profile = Profile(
                user_id=user_id,
                weight=data.get("weight"),
                height=data.get("height"),
                BMR= self.calculate_bmr(data.get("height"), data.get("weight"), age),
                chronic=data.get("chronic"),
                allergies=data.get("allergies"),
                goals=data.get("goals")
            )

            profile = self.profile_repo.create(profile)

        else:
            data["BMR"] = self.calculate_bmr(data.get("height"), data.get("weight"), age),
            profile = self.profile_repo.update(profile, data)

        return profile_schema.dump(profile)

    def get_user_age(self, user_id):
        user = self.user_repo.find_by_id(user_id)
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

    def calculate_bmr(self, height, weight, age):
        return int(
            10 * weight
            + 6.25 * (height * 100)
            - 5 * age
            + 5
        )