from flask import Flask
from app.controllers import users


def create_routes(app: Flask):
    app.add_url_rule("/user/signin", methods=["POST"], view_func=users.signin)
    app.add_url_rule("/user/login", methods=["POST"], view_func=users.login)
    app.add_url_rule("/user/update", methods=["PUT"], view_func=users.update)