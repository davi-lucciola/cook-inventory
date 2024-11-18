from db import db
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, relationship
from app.inventory.enums.measure import Measure
from app.category.category_model import Category


class Inventory(db.Model):
    __tablename__ = 'inventories'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str] = Column(String(255), nullable=True)

    category_id: Mapped[int] = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category: Mapped["Category"] = relationship("Category", foreign_keys=[category_id])

    quantity: Mapped[float]
    alert_quantity: Mapped[float]
    measure: Mapped[Measure] = Column(type_=Enum(Measure), nullable=False)


    def __init__(
        self, 
        name: str, 
        description: str | None, 
        category_id: int, 
        quantity: int, 
        alert_quantity: int | None, 
        measure: Measure
    ) -> None:
        self.name = name
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.alert_quantity = alert_quantity
        self.measure = measure

    @staticmethod
    def validate(data: dict[str, str]):
        if data.get('name') is None or data.get('name').strip('') == '':
            raise ValueError('O campo nome é obrigatório.')
    
        if data.get('category') is None or data.get('category').strip('') == '':
            raise ValueError('O campo categoria é obrigatório.')
        
        if data.get('quantity') is None or data.get('quantity').strip('') == '':
            raise ValueError('O campo quantidade é obrigatório.')
        
        measure_keys = [key for key, _ in Measure.get_values().items()]
        if data.get('measure') is None or data.get('measure').strip('') == '' or data.get('measure') not in measure_keys:
            raise ValueError('O campo unidade de medida é obrigatório.')

        if data.get('measure') == Measure.UNIT.name and (not data.get('quantity').isdigit() or not data.get('alert_quantity').isdigit()):
            raise ValueError('As quantidades devem ser inteiras para a medida por unidade.')
        
        if data.get('alert_quantity').strip('') == '':
            data.update({ 'alert_quantity': None })

        if data.get('description').strip('') == '':
            data.update({ 'description': None })

        data.update({
            # 'category': float(data.get('category')),
            'quantity': float(data.get('quantity')),
            'alert_quantity': float(data.get('alert_quantity'))
        })

        return data