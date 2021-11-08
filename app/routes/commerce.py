from flask import Flask

from app.controllers import commerce


def create_route(app: Flask):
    app.add_url_rule("/commerce/create", methods=["POST"], view_func=commerce.create)
    app.add_url_rule("/commerce/update", methods=["PUT"], view_func=commerce.update)
    app.add_url_rule("/commerce/<int:id>", methods=["GET"], view_func=commerce.get)
    app.add_url_rule("/commerce/list", methods=["GET"], view_func=commerce.list)
    app.add_url_rule("/commerce/search", methods=["POST"], view_func=commerce.search)