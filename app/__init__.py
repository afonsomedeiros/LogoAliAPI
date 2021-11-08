from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

#from .controllers import blue_user, blue_commerce
from .routes import create_routes
from .extensions import sqlalchemy_ext, marshmallow_ext, swagger
from .models.user import User
from .models.commerce import Commerce


def create_app():
    app = Flask(__name__)

    swggr = swagger.install(app)

    create_routes(app)

    app.config['JWT_SECRET_KEY'] = "ChaveJWT"

    sqlalchemy_ext.install(app)
    marshmallow_ext.install(app)

    # app.register_blueprint(blue_user)
    # app.register_blueprint(blue_commerce)
    
    Migrate(app, sqlalchemy_ext.orm)
    JWTManager(app)

    return app