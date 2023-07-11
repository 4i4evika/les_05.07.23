from sqlalchemy import Column, ForeignKey, Integer, String, Table
from models.database import Base
from sqlalchemy.orm import relationship


association_table = Table('association', Base.metadata,
                          Column('customer_id', Integer, ForeignKey('customers.id')),
                          Column('seller_id', Integer, ForeignKey('salesmen.id')))


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    customers_title = Column(String(100), nullable=False)
    salesmen = relationship('Salesmen', secondary='association', backref='customers')

    def __repr__(self):
        return f'Id покупателя: {self.id}, ' \
               f'Наименование покупателя: {self.customers_title}'