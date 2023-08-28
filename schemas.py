from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)