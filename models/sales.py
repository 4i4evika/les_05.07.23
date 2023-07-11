from sqlalchemy import Column, ForeignKey, Integer, String
from models.database import Base


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    seller = Column(String(100), ForeignKey('salesmen.id'))
    count = Column(Integer)
    price = Column(Integer)

    def __init__(self, name, seller_id, count, price):
        self.name = name
        self.seller = seller_id
        self.count = count
        self.price = price
        # self.group = group_id

    def __repr__(self):
        return f'Товар (Наименование: {self.name}, ' \
               f'Продавец: {self.seller} ' \
               f'Количество: {self.count}, ' \
               f'Цена: {self.price}) '