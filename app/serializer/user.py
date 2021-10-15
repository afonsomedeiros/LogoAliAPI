from marshmallow import fields, post_load

from app.extensions.marshmallow_ext import ma
from app.models.user import User


class User_Schema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'created_at', 'updated_at')

    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)