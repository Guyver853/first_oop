from classes.order import Order  # Импортируем класс Order
from classes.product import Product  # Импортируем класс Product
from classes.customer import Customer  # Импортируем класс Customer
from classes.discount import Discount  # Импортируем класс Discount

# Создаем список продуктов с их именами и ценами
products = [
    Product("Novomin", 1000),  # Продукт 1: Novomin
    Product("Calcium", 500),  # Продукт 2: Calcium
    Product("Germanium", 300),  # Продукт 3: Germanium
    Product("Selenium", 200),  # Продукт 4: Selenium
    Product("Iron", 150),  # Продукт 5: Iron
    Product("Betaine", 400),  # Продукт 6: Betaine
    Product("B-complex", 100),  # Продукт 7: B-complex
    Product("Omega-3", 50),  # Продукт 8: Omega-3
    Product("Mega-Essentials", 25),  # Продукт 9: Mega-Essentials
    Product("Lecithin", 80)  # Продукт 10: Lecithin
]

# Создаем список клиентов
customers = [
    Customer("Sergey"),  # Клиент 1: Sergey
    Customer("Vladimir"),  # Клиент 2: Vladimir
    Customer("Marina"),  # Клиент 3: Marina
    Customer("Olga"),  # Клиент 4: Olga
    Customer("Kseniya")  # Клиент 5: Kseniya
]

# Создаем заказы и добавляем их клиентам
orders = [
    Order([products[0]]),  # Заказ 1: Sergey - 1 продукт (Novomin)
    Order([products[1], products[2]]),  # Заказ 2: Vladimir - 2 продукта (Calcium, Germanium)
    Order([products[3], products[4], products[5]]),  # Заказ 3: Marina - 3 продукта (Selenium, Iron, Betaine)
    Order([products[6], products[7], products[8], products[9]]), # Заказ 4: Olga - 4 продукта (B-complex, Omega-3, Mega-Essentials, Lecithin)
    Order([products[0], products[1], products[2], products[3], products[4]]) # Заказ 5: Kseniya - 5 продуктов (Novomin, Calcium, Germanium, Selenium, Iron)
]

# Добавляем заказы к соответствующим клиентам
customers[0].add_order(orders[0])  # Sergey
customers[1].add_order(orders[1])  # Vladimir
customers[2].add_order(orders[2])  # Marina
customers[3].add_order(orders[3])  # Olga
customers[4].add_order(orders[4])  # Kseniya

# Создаем скидки
seasonal_discount = Discount("Сезонная скидка", 10)  # Сезонная скидка 10%
sale_discount = Discount("Скидка-распродажа", 20)  # Скидка-распродажа 20%
gift_discount = Discount("Скидка-подарок", 25)  # Скидка-подарок 25%

# Применяем скидки к заказам клиентов, выводим информацию
for customer in customers:
    total_spent = 0  # Счетчик общей суммы заказов клиента
    for order in customer.orders:  # Проходим по каждому заказу клиента
        original_price = order.total_price()  # Получаем оригинальную цену заказа

        # Применяем различные скидки в зависимости от количества продуктов в заказе
        if len(order.products) >= 5:
            discounted_price = Discount.apply_discount(original_price, gift_discount.discount_percent)  # Скидка-подарок
        elif len(order.products) == 4:
            discounted_price = Discount.apply_discount(original_price,
                                                       sale_discount.discount_percent)  # Скидка-распродажа
        else:
            discounted_price = Discount.apply_discount(original_price,
                                                       seasonal_discount.discount_percent)  # Сезонная скидка

        total_spent += discounted_price  # Суммируем итоговую стоимость заказа
        print(
            f"{customer.name} - {order} (Оригинальная цена: {original_price:.2f}, Цена со скидкой: {discounted_price:.2f})")

    print(f"Итого сумма заказов для {customer.name}: {total_spent:.2f}")  # Выводим итоговую сумму по заказам клиента

# Подсчет общего количества заказов и общей суммы всех заказов
total_orders_count = sum(len(customer.orders) for customer in customers)  # Подсчет общего количества заказов
total_amount_spent = sum(order.total_price() for customer in customers for order in customer.orders)  # Подсчет общей суммы всех заказов

# Выводим общее количество заказов и общую сумму
print(f"\nВсего заказов: {total_orders_count}")  # Выводим общее количество заказов
print(f"Общая сумма всех заказов: {total_amount_spent:.2f}")  # Выводим общую сумму всех заказов

# Вывод информации о клиентах с использованием дандер методов
for customer in customers:
    print(customer)  # Выводим информацию о каждом клиенте, которая может быть реализована в __str__ методе

"""
1. Импорт классов: Импортируются необходимые классы для работы с продуктами, клиентами, заказами и скидками.

2. Создание продуктов: Создается массив продуктов с названиями и ценами.

3. Создание клиентов: Создается массив клиентов.

4. Создание и добавление заказов:
  Заказы создаются с помощью класса Order, содержащего различные продукты.
  Каждому заказу добавляются клиенты.
  
5. Создание скидок: Создаются три типа скидок: сезонная, распродажа и подарок.

6. Применение скидок и вывод информации:
   Для каждого клиента и его заказов вычисляются оригинальная цена и цена со скидкой.
   Применяются различные скидки в зависимости от количества продуктов в заказе.
   Итоговая сумма, потраченная каждым клиентом, суммируется и выводится.
   
7. Подсчет общего количества заказов и суммы:
   Общее количество заказов подсчитывается с использованием генератора списков.
   Общая сумма потраченных средств вычисляется через сумму всех оригинальных цен всех заказов.
   
8. Вывод информации о клиентах: Выводится информация о клиентах, которая может быть реализована в методе __str__ классов клиентов.
"""