from marshmallow import Schema, fields, ValidationError, validates_schema

CORRECT_CMD = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')


class Request(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema()
    def validate_param(self, values, *args, **kwargs) -> None:
        if values['cmd'] not in CORRECT_CMD:
            raise ValidationError("your request does not match the requirements")


class BatchRequest(Schema):
    queries = fields.Nested(Request, many=True)
