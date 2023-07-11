from sqlalchemy import Column, Integer, String
from models.database import Base
from sqlalchemy.orm import relationship


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True, autoincrement=True)
    seller = Column(String(100), nullable=False)
    sales = relationship('Sales')

    def __repr__(self):
        return f'Id продавца: {self.id}, ' \
               f'Название продавца: {self.seller}'