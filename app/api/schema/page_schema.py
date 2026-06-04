from marshmallow import Schema, fields, validate

class PageSchema(Schema):
    page = fields.Int(load_default=1, validate=validate.Range(min=1))
    page_size = fields.Int(load_default=10, validate=validate.Range(min=1, max=100))
