from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from marshmallow import ValidationError

from app.api.schema.user_schema import SignUpSchema, SignInSchema
from app.resp import succeed, fail
from app.service.user_service import UserService
from app.repository.user_repo import UserRepository
from exception import NutriCoachException

user_bp = Blueprint("user", __name__)
user_repository = UserRepository()
user_service = UserService(user_repository)


@user_bp.route("/user/sign-up", methods=["POST"])
def sign_up():
    try:
        schema = SignUpSchema()
        data = schema.validate(request.json)
        resp = user_service.sign_up(data)
        return succeed(resp.to_dict())
    except ValidationError as e:
        return fail(code=400, message=e.messages)
    except NutriCoachException as e:
        return fail(code=1, message=str(e))
    except Exception as e:
        return fail(code=1, message="Unknown error")


@user_bp.route("/user/sign-in", methods=["POST"])
def sign_in():
    try:
        schema = SignInSchema()
        data = schema.validate(request.json)
        user = user_service.sign_in(data)
        access_token = create_access_token(
            identity=str(user.id)
        )
        return succeed({
            "token": access_token,
            "user": user.to_dict()
        })
    except ValidationError as e:
        return fail(code=400, message=e.messages)
    except NutriCoachException as e:
        return fail(code=1, message=str(e))
    except Exception as e:
        return fail(code=1, message="Unknown error")



@user_bp.route("/user/me", methods=["GET"])
@jwt_required()
def get_current_user():
    try:
        user_id = get_jwt_identity()

        resp = user_service \
            .get_current_user(user_id)

        return succeed(resp.to_dict())
    except NutriCoachException as e:
        return fail(code=1, message=str(e))
    except Exception as e:
        return fail(code=1, message="Unknown error")


@user_bp.route("/user/delete-account", methods=["DELETE"])
@jwt_required()
def delete_account():
    try:
        user_id = get_jwt_identity()
        user_service \
            .delete_account(user_id)
        return succeed(True)
    except NutriCoachException as e:
        return fail(code=1, message=str(e))
    except Exception as e:
        return fail(code=1, message="Unknown error")