from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate


class GenerateDietPlanRequestSchema(Schema):

    budget = fields.Float(
        required=True,
        validate=validate.Range(
            min=1,
            error="budget must be greater than 0"
        )
    )

class DietPlanSchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    user_id = fields.Int(
        dump_only=True
    )

    breakfast = fields.List(
        fields.String()
    )

    lunch = fields.List(
        fields.String()
    )

    snack = fields.List(
        fields.String()
    )

    dinner = fields.List(
        fields.String()
    )

    create_time = fields.DateTime(
        dump_only=True
    )