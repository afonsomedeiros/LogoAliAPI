from flask_sqlalchemy import SQLAlchemy

from CONST import ROOT_PATH

orm = SQLAlchemy()


def install(app):
    #app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{ROOT_PATH}/database.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://afonso2k:LOGOALIAPI123@afonso2k.mysql.pythonanywhere-services.com/afonso2k$LOGOALI"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    orm.init_app(app)
    app.db = orm