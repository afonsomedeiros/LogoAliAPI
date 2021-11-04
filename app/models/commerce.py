from sqlalchemy.orm import backref
from app.extensions.sqlalchemy_ext import orm as DB
from datetime import datetime


class Commerce(DB.Model):
    __tablename__ = "Commerces"
    id = DB.Column("idCommerce", DB.Integer, primary_key = True)
    id_user = DB.Column("ID_USER", DB.Integer, DB.ForeignKey("Users.idUser"))
    trading_name = DB.Column("tradingName", DB.String(70))
    company_name = DB.Column("companyName", DB.String(70))
    cover_path = DB.Column("coverPath", DB.String(200))
    segment = DB.Column(DB.String(30), nullable=False)
    description = DB.Column(DB.String(500))
    cell_number = DB.Column("cellNumber", DB.String(20))
    email = DB.Column(DB.String(200))
    street = DB.Column(DB.String(120))
    number = DB.Column(DB.Integer)
    complement = DB.Column(DB.String(50))
    neighborhood = DB.Column(DB.String(50))
    city = DB.Column(DB.String(50))
    state = DB.Column(DB.String(50))
    zipcode = DB.Column(DB.String(12))
    created_at = DB.Column("createdAt", DB.DateTime, default=datetime.utcnow)
    updated_at = DB.Column("updatedAt", DB.DateTime, onupdate=datetime.utcnow)