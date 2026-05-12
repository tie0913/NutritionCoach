from app.repository.user_repo import find_user

def get_user(user_id):
    user = find_user(user_id)

    return {
        "code": 0,
        "message": "success",
        "data": user
    }