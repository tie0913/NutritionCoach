from app import db
from app.model.profile import Profile


class ProfileRepository:


    def get_by_user_id(self, user_id):
        return Profile.query.filter_by(user_id=user_id).first()

    def create(self, profile):
        db.session.add(profile)
        db.session.commit()
        return profile

    def update(self, profile, data):
        for key, value in data.items():
            setattr(profile, key, value)
        db.session.commit()
        return profile