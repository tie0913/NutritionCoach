from marshmallow import ValidationError

from app.model.profile import Profile
from app.repository.profile_repo import ProfileRepository
from app.api.schema.profile_schema import profile_schema


class ProfileService:

    def __init__(self, profile_repo):
        self.profile_repo = profile_repo

    def get_profile(self, user_id):
        return self.profile_repo.get_by_user_id(user_id)

    def save_profile(self, user_id, data):

        profile = self.profile_repo.get_by_user_id(user_id)

        if profile is None:
            profile = Profile(
                user_id=user_id,
                weight=data.get("weight"),
                height=data.get("height"),
                BMR=data.get("BMR"),
                chronic=data.get("chronic"),
                allergies=data.get("allergies"),
                goals=data.get("goals")
            )

            profile = self.profile_repo.create(profile)

        else:
            profile = self.profile_repo.update(profile, data)

        return profile_schema.dump(profile)