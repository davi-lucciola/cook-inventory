from db import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    fl_active = Column(Boolean, nullable=False, default=True)
		
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = generate_password_hash(password)
    
    def verify_password(self, plain_password: str) -> bool:
        return check_password_hash(self.password, plain_password)
    