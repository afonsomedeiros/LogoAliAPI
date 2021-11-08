from flask import Blueprint, jsonify, Response, request, current_app
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from app.models.user import User
from app.serializer.user import User_Schema

#blue_user = Blueprint("user", __name__, url_prefix="/user")


#@blue_user.post("/signin")
def signin():
    """
        path: /user/signin
        method: POST
        Contract: {
            "name": "Afonso Medeiros",
            "email": "afonso@afonso.com",
            "password": "123456"
        }
        Response: {
            "created_at": "",
            "email": "",
            "id": 0,
            "name": "",
            "password": "",
            "updated_at": null
        }
    """
    try:
        us = User_Schema()
        user = us.load(request.json)

        user.gen_hash()

        current_app.db.session.add(user)
        current_app.db.session.commit()
        Response.content_type = 'Application/json'
        return us.jsonify(user), 201
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})

#@blue_user.post("/login")
def login():
    """
        path: /user/login
        method: POST
        Contract: {
            "email": "afonso@afonso.com",
            "password": "123456"
        }
        Response: {
            'access_token': "",
            'refresh_token': "",
            'message': ""
        }
    """
    try:
        email, password = request.json['email'], request.json['password']
        user = User.query.filter_by(email=email).first()
        if user and user.verify(password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return jsonify({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'message': "Login succefull!"
            }), 200
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})


#@blue_user.put("update")
@jwt_required
def update():
    """
        path: /user/update
        method: PUT
        Contract: {
            "name": "Afonso Medeiros",
            "email": "afonso@afonso.com"
        }

        Header:
            Authorization: Bearer <access_token>
    """
    try:
        user = User.query.filter_by(id=get_jwt_identity()).first()
        user.name = request.json['name']
        user.email = request.json['email']
        current_app.db.session.commit()
        return User_Schema.jsonify(user)
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})