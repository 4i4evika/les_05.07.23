from faker import Faker

from models.database import create_db, Session
from models.sales import Sales
from models.salesmen import Salesmen
from models.customers import Customers


# Функция для создания базы данных
def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    customers = ['1111', '2222', '3333', '4444',
               '5555', '6666', '7777']

    group1 = Salesmen(seller='ООО Ромашка')
    group2 = Salesmen(seller='ОАО Лютик')
    session.add(group1)
    session.add(group2)

    for key, les in enumerate(customers):
        customer = Customers(customers_title=les)
        customer.salesmen.append(group1)
        if key % 2 == 0:
            customer.salesmen.append(group2)
        session.add(customer)

    session.commit()
    faker = Faker('ru_RU')
    groups = [group1, group2]

    for _ in range(20):
        name = faker.random_element(elements=['вафли', 'кофеты', 'печенье'])
        count = faker.random.randint(1, 25)
        price = faker.random.randint(1, 1000)
        salesmen = faker.random.choice(groups)
        sales = Sales(name, salesmen.id, count, price)
        session.add(sales)

    session.commit()
    session.close()
