from flask_marshmallow import Marshmallow


ma = Marshmallow()


def install(app):
    ma.init_app(app)