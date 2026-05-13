from app.model.user import User


def find_user(user_id) -> User:
    return User.query.get(user_id)
