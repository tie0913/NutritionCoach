from app.model.user import User
from app import db

class UserRepository:

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
