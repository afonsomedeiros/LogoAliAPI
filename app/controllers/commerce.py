from operator import or_
from flask import Blueprint, blueprints, jsonify, Response, request, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import or_

from app.models.commerce import Commerce
from app.models.user import User
from app.serializer.commerce import Commerce_Schema


blue_commerce = Blueprint("commerce", __name__, url_prefix="/commerce")


@blue_commerce.post("/create")
@jwt_required()
def create():
    """
        Contract: {
            "trading_name": "",
            "company_name": "",
            "cover_path": "",
            "segment": "",
            "description": "",
            "cell_number": "",
            "email": "",
            "street": "",
            "number": "",
            "complement": "",
            "neighborhood": "",
            "city": "",
            "state": "",
            "zipcode": ""
        }
        Header:
            Authorization: Bearer <access_token>
    """
    try:
        user = User.query.filter_by(id=get_jwt_identity()).first()
        cs = Commerce_Schema()
        commerce = cs.load(request.json)
        commerce.id_user = user.id
        current_app.db.session.add(commerce)
        current_app.db.session.commit()
        return cs.jsonify(commerce), 201
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})


@blue_commerce.put("/update")
@jwt_required()
def update():
    """
        Contract: {
            "id": "",
            "trading_name": "",
            "company_name": "",
            "cover_path": "",
            "segment": "",
            "description": "",
            "cell_number": "",
            "email": "",
            "street": "",
            "number": "",
            "complement": "",
            "neighborhood": "",
            "city": "",
            "state": "",
            "zipcode": ""
        }
        Header:
            Authorization: Bearer <access_token>
    """
    try:
        data = request.json
        commerce = Commerce.query.filter_by(id = data["id"]).first()
        commerce.trading_name = data["trading_name"]  if 'trading_name' in data else ""
        commerce.company_name =  data["company_name"] if 'company_name' in data else ""
        commerce.cover_path =  data["cover_path"] if 'cover_path' in data else ""
        commerce.segment =  data["segment"] if 'segment' in data else ""
        commerce.description =  data["description"] if 'description' in data else ""
        commerce.cell_number =  data["cell_number"] if 'cell_number' in data else ""
        commerce.email =  data["email"] if 'email' in data else ""
        commerce.street =  data["street"] if 'street' in data else ""
        commerce.number =  data["number"] if 'number' in data else ""
        commerce.complement =  data["complement"] if 'complement' in data else ""
        commerce.neighborhood =  data["neighborhood"] if 'neighborhood' in data else ""
        commerce.city =  data["city"] if 'city' in data else ""
        commerce.state =  data["state"] if 'state' in data else ""
        commerce.zipcode =  data["zipcode"] if 'zipcode' in data else ""
        current_app.db.session.commit()
        return Commerce_Schema().jsonify(commerce)
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})


@blue_commerce.get("/<int:id>")
def get(id: int):
    """
        Busca Comercio/Serviço através do ID:
        url: /commerce/1
    """
    try:
        commerce = Commerce.query.filter_by(id = id).first()
        return Commerce_Schema().jsonify(commerce)
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})


@blue_commerce.get("list")
def list():
    """
        Lista todas as categorias em ordem decrescente pelo ID.
        busca pode ser paginada e limitada utilizando parametros na URL
        exemplo:
            /commerce/list?page=1
            /commerce/list?per_page=500
            /commerce/list?page=5&per_page=5
    """
    try:
        page = request.args.get("page") if bool(request.args.get("page")) else 1
        limit = request.args.get("limit") if bool(request.args.get("limit")) else 10
        limit = limit if int(limit) <= 1000 else 1000
        commerces = Commerce.query.order_by(Commerce.id.desc()).paginate(page, limit, error_out=False)
        schema = Commerce_Schema(many=True).dump(commerces.items)
        total_pages = round(commerces.total / limit)
        result_obj = {
            "page": str(page),
            "per_page": str(limit),
            "total_pages": total_pages if total_pages > 0 else 1,
            "total_results": commerces.total,
            "commerces": schema
        }
        return jsonify(result_obj), 200
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})


@blue_commerce.post("/search")
def search():
    """
        Realiza busca utilizando campo "search".
        Consulta se o conteudo do campo "search" está presente nos campos:
            company_name,
            trading_name,
            zipcode,
            city,
            complement,
            description,
            cell_number,
            email,
            neighborhood,
            segment,
            state,
            street
        Da tabela Commerces
    """
    page = request.args.get("page") if bool(request.args.get("page")) else 1
    limit = request.args.get("limit") if bool(request.args.get("limit")) else 10
    # Busca
    try:
        content_search = request.json['search']
        commerces = Commerce.query.filter(
            or_(
                Commerce.company_name.contains(content_search),
                Commerce.trading_name.contains(content_search),
                Commerce.zipcode.contains(content_search),
                Commerce.city.contains(content_search),
                Commerce.complement.contains(content_search),
                Commerce.description.contains(content_search),
                Commerce.cell_number.contains(content_search),
                Commerce.email.contains(content_search),
                Commerce.neighborhood.contains(content_search),
                Commerce.segment.contains(content_search),
                Commerce.state.contains(content_search),
                Commerce.street.contains(content_search)
            )
        ).paginate(page, limit, error_out=False)
        schema = Commerce_Schema(many=True).dump(commerces.items)
        total_pages = round(commerces.total / limit)
        result_obj = {
            "page": str(page),
            "per_page": str(limit),
            "total_pages": total_pages if total_pages > 0 else 1,
            "total_results": commerces.total,
            "commerces": schema
        }
        return jsonify(result_obj), 200
    except BaseException as e:
        return jsonify({'err': str(type(e)), 'message': str(e)})