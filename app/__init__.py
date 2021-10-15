from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from .controllers import blue_user
from .extensions import sqlalchemy_ext, marshmallow_ext
from .models.user import User


def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = "ChaveJWT"

    sqlalchemy_ext.install(app)
    marshmallow_ext.install(app)

    app.register_blueprint(blue_user)
    
    Migrate(app, sqlalchemy_ext.orm)
    JWTManager(app)

    return app