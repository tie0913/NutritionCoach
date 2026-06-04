from flask import Blueprint
from flask import request

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.api.schema.page_schema import PageSchema
from app.api.schema.plan_schema import (
    GenerateDietPlanRequestSchema,
    DietPlanSchema
)

from app.service.plan_service import PlanService

from app.resp import succeed, fail


plan_bp = Blueprint(
    "plan",
    __name__,
    url_prefix="/plan"
)

@plan_bp.post("")
@jwt_required()
def generate_plan():

    request_data = GenerateDietPlanRequestSchema().load(
        request.json
    )

    user_id = get_jwt_identity()

    plan = PlanService.generate_plan(
        user_id=user_id,
        budget=request_data["budget"]
    )

    return succeed(
        DietPlanSchema().dump(plan)
    )


@plan_bp.get("")
@jwt_required()
def list_plan():

    query = PageSchema().load(
        request.args
    )

    user_id = get_jwt_identity()

    result = PlanService.list_plan(
        user_id=user_id,
        page=query["page"],
        page_size=query["page_size"]
    )

    return succeed({
        "items": DietPlanSchema(
            many=True
        ).dump(result.items),

        "page": result.page,
        "page_size": result.per_page,
        "total": result.total,
        "pages": result.pages
    })