from db import db
from sqlalchemy import Column, Integer, String


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    
    def __init__(self, name: str, description: str | None = None) -> None:
        self.name = name
        self.description = description

    def update(self, data: dict):
        self.name = data.get('name')
        self.description = data.get('description')