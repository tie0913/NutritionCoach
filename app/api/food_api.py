# app/controllers/food_controller.py
import traceback
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from flask import Blueprint, request, jsonify, g
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from app.api.schema.food_schema import (
    FoodCreateSchema,
    DiagramQuerySchema, FoodDeleteSchema,
)
from app.api.schema.page_schema import PageSchema
from app.service.food_service import FoodService
from app.repository.food_repo import FoodRepository
from app.resp import succeed, fail

food_repo = FoodRepository()
food_svc = FoodService(food_repo)


food_bp = Blueprint("food", __name__)


@food_bp.route("/foodlog", methods=["POST"])
@jwt_required()
def create_food():
    try:
        user_id = int(get_jwt_identity())
        data = FoodCreateSchema().load(request.get_json() or {})

        result = food_svc.create_food(user_id, data)
        return succeed(result), 201

    except ValidationError as e:
        return fail(code=1, message=str(e.messages)), 400

    except Exception as e:
        traceback.print_exc()
        return fail(code=1, message="Server error"), 500


@food_bp.route("/foodlog", methods=["GET"])
@jwt_required()
def list_foods():
    try:
        user_id = int(get_jwt_identity())
        query = PageSchema().load(request.args)

        result = food_svc.list_foods(
            user_id=user_id,
            page=query["page"],
            page_size=query["page_size"]
        )

        return succeed(result), 200

    except ValidationError as e:
        return fail(code=1, message=str(e.messages)), 400

    except Exception as e:
        traceback.print_exc()
        return fail(code=1, message="Server error"), 500

@food_bp.route("/foodlog", methods=["DELETE"])
@jwt_required()
def delete_food():
    try:
        user_id = int(get_jwt_identity())
        delete = FoodDeleteSchema().load(request.args)
        print(delete)
        record_id = delete["id"]
        res = food_svc.delete_food_log_by_id(user_id, record_id)
        return succeed(res), 200
    except ValidationError as e:
        return fail(code=1, message=str(e.messages)), 400
    except Exception as e:
        traceback.print_exc()
        return fail(code=1, message="Server error"), 500


@food_bp.route("/diagram", methods=["GET"])
@jwt_required()
def get_diagram():
    try:
        user_id = int(get_jwt_identity())
        query = DiagramQuerySchema().load(request.args)

        if query["start_date"] > query["end_date"]:
            return fail("start_date cannot be later than end_date"), 400
        tz = ZoneInfo(g.timezone)

        local_start = datetime.combine(
            query["start_date"],
            datetime.min.time(),
            tzinfo=tz
        )

        local_end = datetime.combine(
            query["end_date"] + timedelta(days=1),
            datetime.min.time(),
            tzinfo=tz
        )

        utc_start = local_start.astimezone(
            timezone.utc
        )

        utc_end = local_end.astimezone(
            timezone.utc
        )
        foods = food_svc.get_diagram_data(
            user_id=user_id,
            start_date=utc_start,
            end_date=utc_end,
        )

        result = summarize_foods_by_day(foods, g.timezone)

        return succeed(result), 200

    except ValidationError as e:
        return fail(code=1, message=str(e.messages)), 400

    except Exception as e:
        traceback.print_exc()
        return fail(code=1, message="Server error"), 500


def summarize_foods_by_day(foods, timezone_name):
    result = defaultdict(
        lambda: {
            "calories": 0,
            "carbs": 0,
            "protein": 0,
            "fats": 0
        }
    )

    tz = ZoneInfo(timezone_name)

    for food in foods:

        create_time = food.create_time

        if create_time.tzinfo is None:
            create_time = create_time.replace(
                tzinfo=timezone.utc
            )

        local_date = (
            create_time
            .astimezone(tz)
            .date()
        )

        result[local_date]["calories"] += food.calories
        result[local_date]["carbs"] += food.carbs
        result[local_date]["protein"] += food.protein
        result[local_date]["fats"] += food.fats

    return [
        {
            "date": date.isoformat(),
            **summary
        }
        for date, summary in sorted(result.items())
    ]
