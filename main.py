# Создайте трёхтабличную базу данных Sales (продажи). В этой базе данных должны быть следующие таблицы
# Sales (информация о конкретных продажах), Salesmen (информация о продавцах), Customers (информация о
# покупателях). Создайте приложение для отображения данных из таблиц. Меню приложения должно содержать
# такой минимальный набор отчётов:
# ■ Отображение всех сделок;
# ■ Отображение сделок конкретного продавца;
# ■ Отображение максимальной по сумме сделки;
# ■ Отображение минимальной по сумме сделки;
# ■ Отображение максимальной по сумме сделки для конкретного продавца;
# ■ Отображение минимальной по сумме сделки для конкретного продавца;
# ■ Отображение максимальной по сумме сделки для конкретного покупателя;
# ■ Отображение минимальной по сумме сделки для конкретного покупателя;
# ■ Отображение продавца, у которого максимальная сумма продаж по всем сделкам;
# ■ Отображение продавца, у которого минимальная сумма продаж по всем сделкам;
# ■ Отображение покупателя, у которого максимальная сумма покупок по всем сделкам;
# ■ Отображение средней суммы покупки для конкретного покупателя;
# ■ Отображение средней суммы покупки для конкретного продавца.
# Добавьте механизмы для обновления, удаления и вставки данных в базу данных используя интерфейс меню.
# Пользователь не может ввести запросы INSERT, UPDATE, DELETE напрямую. Запретите возможность обновления
# и удаления всех данных для каждой из таблиц (UPDATE и DELETE без условий).
# Добавьте к первому заданию возможность сохранения результатов фильтров в файл. Путь и название к файлу
# указываются в настройках приложения.

import os

from sqlalchemy import or_, not_, desc, func, text
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.sales import Sales
from models.salesmen import Salesmen
from models.customers import Customers, association_table


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    while True:
        menu = ('Отображение всех сделок',
                'Отображение сделок конкретного продавца',
                'Отображение максимальной по сумме сделки',
                'Отображение минимальной по сумме сделки',
                'Отображение максимальной по сумме сделки для конкретного продавца',
                'Отображение минимальной по сумме сделки для конкретного продавца',
                'Отображение продавца, у которого минимальная сумма продаж по всем сделкам',
                'Отображение продавца, у которого максимальная сумма продаж по всем сделкам',
                'Отображение средней суммы покупки для конкретного продавца',
                'Добавление данных')

        count = 0
        print('-------------------------------------------------------------------------------')
        for i in menu:
            count += 1
            print(count, " - ", i)
        print()

        x = int(input('Выберите действие, которое вы хотите выполнить: '))
        if x == 1:
            print(session.query(Sales).all())
        elif x == 2:
            x1 = int(input('Выберите продавца (1. ООО Ромашка, 2. ОАО Лютик): '))
            if x1 == 1:
                print(session.query(Sales).filter(Sales.seller.in_(['1'])).all())
            elif x1 == 2:
                print(session.query(Sales).filter(Sales.seller.in_(['2'])).all())
            else:
                print('Введена неверная команда')
        elif x == 3:
            for it in session.query(Sales.name, func.max(Sales.price)):
                print(it)
        elif x == 4:
            for it in session.query(Sales.name, func.min(Sales.price)):
                print(it)
        elif x == 5:
            x2 = int(input('Выберите продавца (1. ООО Ромашка, 2. ОАО Лютик): '))
            if x2 == 1:
                for it in session.query(Sales.name, func.max(Sales.price)).filter(Sales.seller == '1'):
                    print(it)
            elif x2 == 2:
                for it in session.query(Sales.name, func.max(Sales.price)).filter(Sales.seller == '2'):
                    print(it)
            else:
                print('Введена неверная команда')
        elif x == 6:
            x3 = int(input('Выберите продавца (1. ООО Ромашка, 2. ОАО Лютик): '))
            if x3 == 1:
                for it in session.query(Sales.name, func.min(Sales.price)).filter(Sales.seller == '1'):
                    print(it)
            elif x3 == 2:
                for it in session.query(Sales.name, func.min(Sales.price)).filter(Sales.seller == '2'):
                    print(it)
            else:
                print('Введена неверная команда')
        elif x == 7:
            for it in session.query(Salesmen.seller, func.sum(Sales.price)).join(Salesmen).group_by(Salesmen.seller).order_by(desc(Salesmen.seller)).limit(1):
                print(it)
        elif x == 8:
            for it in session.query(Salesmen.seller, func.sum(Sales.price)).join(Salesmen).group_by(Salesmen.seller).limit(1):
                print(it)
        elif x == 9:
            x4 = int(input('Выберите продавца (1. ООО Ромашка, 2. ОАО Лютик): '))
            if x4 == 1:
                for it in session.query(func.avg(Sales.price)).filter(Sales.seller == '1'):
                    print(it)
            elif x4 == 2:
                for it in session.query(func.avg(Sales.price)).filter(Sales.seller == '2'):
                    print(it)
            else:
                print('Введена неверная команда')
        elif x == 10:
            a = Customers(customers_title='888')
            session.add(a)
            session.commit()
            print('Данные добавлены')

        else:
            break