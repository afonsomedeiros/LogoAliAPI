from app.extensions.sqlalchemy_ext import orm as DB
from passlib.hash import pbkdf2_sha512 as sha
from datetime import datetime


class User(DB.Model):
    __tablename__ = "Users"
    id = DB.Column("idUser", DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(120), nullable=False)
    password = DB.Column(DB.String(200), nullable=False)
    created_at = DB.Column("createdAt", DB.DateTime, default=datetime.utcnow)
    updated_at = DB.Column("updatedAt", DB.DateTime, onupdate=datetime.utcnow)

    def gen_hash(self):
        self.password = sha.hash(self.password)

    def verify(self, password):
        return sha.verify(password, self.password)