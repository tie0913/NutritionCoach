from app.model.user import User
from app.repository.user_repo import find_user


def get_user(user_id) -> User:
    return find_user(user_id)
