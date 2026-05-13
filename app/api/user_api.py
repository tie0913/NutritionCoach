from flask import Blueprint

from app.resp import succeed

from app.service.user_service import get_user

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/user"
)


@user_bp.route("/<int:user_id>", methods=["GET"])
def query_user(user_id):
    user = get_user(user_id)
    return succeed(user.to_dict())
