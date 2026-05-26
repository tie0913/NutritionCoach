from marshmallow import fields, validate, Schema


class ProfileSchema(Schema):
    id = fields.Int(dump_only=True)

    user_id = fields.Int(dump_only=True)

    weight = fields.Float(
        required=False,
        allow_none=True,
        validate=validate.Range(min=0)
    )

    height = fields.Float(
        required=False,
        allow_none=True,
        validate=validate.Range(min=0)
    )

    BMR = fields.Int(
        required=False,
        allow_none=True,
        validate=validate.Range(min=0)
    )

    chronic = fields.List(
        fields.String(),
        required=False,
        allow_none=True
    )

    allergies = fields.List(
        fields.String(),
        required=False,
        allow_none=True
    )

    goals = fields.List(
        fields.String(),
        required=False,
        allow_none=True
    )


profile_schema = ProfileSchema()