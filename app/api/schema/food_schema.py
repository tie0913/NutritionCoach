from marshmallow import Schema, fields, validate

from app.api.schema.local_date_time import LocalDateTime


class FoodCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    quantity = fields.Float(required=True, validate=validate.Range(min=0))
    calories = fields.Int(required=True, validate=validate.Range(min=0))
    carbs = fields.Int(required=True, validate=validate.Range(min=0))
    protein = fields.Int(required=True, validate=validate.Range(min=0))
    fats = fields.Int(required=True, validate=validate.Range(min=0))


class FoodResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    name = fields.Str()
    quantity = fields.Float()
    calories = fields.Int()
    carbs = fields.Int()
    protein = fields.Int()
    fats = fields.Int()
    create_time = LocalDateTime()




class FoodDeleteSchema(Schema):
    id = fields.Int()

class DiagramQuerySchema(Schema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

