# app/schemas/food_schema.py

from marshmallow import Schema, fields, validate


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
    create_time = fields.DateTime()


class FoodQuerySchema(Schema):
    page = fields.Int(load_default=1, validate=validate.Range(min=1))
    page_size = fields.Int(load_default=10, validate=validate.Range(min=1, max=100))


class DiagramQuerySchema(Schema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)