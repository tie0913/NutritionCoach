from marshmallow import Schema, fields, validate, validates_schema, ValidationError

class SignInSchema(Schema):

    email = fields.Email(
        required=True
    )

    password = fields.Str(
        required=True,
        validate=validate.Length(min=6),
        load_only=True
    )

class SignUpSchema(Schema):

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=50)
    )

    email = fields.Email(
        required=True
    )

    password = fields.Str(
        required=True,
        validate=validate.Length(min=6, max=128),
        load_only=True
    )

    confirm_password = fields.Str(
        required=True,
        load_only=True
    )

    birth_date = fields.Date(
        required=True
    )

    @validates_schema
    def validate_password_match(self, data, **kwargs):

        if data["password"] != data["confirm_password"]:
            raise ValidationError(
                {"confirm_password": ["Passwords do not match."]}
            )