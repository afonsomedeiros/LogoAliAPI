from marshmallow import post_load
from marshmallow.decorators import post_dump

from app.extensions.marshmallow_ext import ma
from app.models.commerce import Commerce
from app.models.user import User


class Commerce_Schema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_user",
            "trading_name",
            "company_name",
            "cover_path",
            "segment",
            "description",
            "cell_number",
            "email",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
            "zipcode",
            "created_at",
            "updated_at",
        )

    @post_load
    def make_commerce(self, data, **kwargs):
        return Commerce(**data)

    @post_dump(pass_many=True)
    def serialize(self, data, many, **kwargs):
        if type(data) is not dict:
            for commerce in data:
                user = User.query.filter_by(id=commerce["id_user"]).first()
                commerce['user'] = {
                    'name': user.name,
                    'email': user.email
                }
        return data