from flask import Flask

from . import user
from . import commerce

def create_routes(app: Flask):
    user.create_routes(app)
    commerce.create_route(app)