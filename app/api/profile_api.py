from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from app.api.schema.profile_schema import profile_schema
from app.service.profile_service import ProfileService
from app.repository.profile_repo import ProfileRepository
from app.resp import succeed, fail

profile_repo = ProfileRepository()
profile_service = ProfileService(profile_repo)

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/profile"
)


@profile_bp.route("", methods=["GET"])
@jwt_required()
def get_profile():

    try:
        user_id = get_jwt_identity()

        profile = profile_service.get_profile(user_id)

        if profile is None:
            return fail("Profile not found"), 404

        return succeed(profile_schema.dump(profile)), 200

    except Exception as e:
        return fail(str(e)), 500


@profile_bp.route("", methods=["POST"])
@jwt_required()
def save_profile():

    try:
        user_id = get_jwt_identity()
        json_data = request.get_json()
        data = profile_schema.load(json_data)
        profile = profile_service.save_profile(
            user_id,
            json_data
        )
        return succeed(profile), 200
    except ValidationError as e:
        return fail(str(e)), 400

    except Exception as e:
        return fail(str(e)), 500