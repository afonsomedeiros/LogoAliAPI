from flask_sqlalchemy import SQLAlchemy


orm = SQLAlchemy()


def install(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    orm.init_app(app)
    app.db = orm