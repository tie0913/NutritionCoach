from app.model.user import User
from app import db

class UserRepository:

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user

    def find_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def find_by_id(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
