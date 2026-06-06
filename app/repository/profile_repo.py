from app import db
from app.model.profile import Profile


class ProfileRepository:


    @staticmethod
    def get_by_user_id(user_id):
        return Profile.query.filter_by(user_id=user_id).first()

    @staticmethod
    def create(profile):
        db.session.add(profile)
        db.session.commit()
        return profile

    @staticmethod
    def update(profile, data):
        for key, value in data.items():
            setattr(profile, key, value)
        db.session.commit()
        return profile