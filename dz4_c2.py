# ДЗ 4.1. ООП
# Примітивна система управління магазином


class Product:
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def change_price(self, new_price: float) -> None:
        """Змінює ціну товару"""
        self.price = new_price

    def change_stock(self, new_stock: int) -> None:
        """Змінює кількість товару на складі"""
        self.stock = new_stock


class Order:
    def __init__(self):
        self.products: list[tuple[Product, int]] = []
        self.total_amount: float = 0.0

    def add_product(self, product: Product, quantity: int) -> None:
        """Додає товар до замовлення"""
        if quantity > product.stock:
            print(f"Недостатньо товару на складі: {product.name}")
            return

        self.products.append((product, quantity))
        self.total_amount += product.price * quantity
        product.change_stock(product.stock - quantity)

    def calculate_total(self) -> None:
        """Обчислює загальну суму замовлення"""
        self.total_amount = sum(
            product.price * quantity
            for product, quantity in self.products
        )


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.orders: list[Order] = []

    def add_order(self, order: Order) -> None:
        """Додає замовлення клієнту"""
        self.orders.append(order)


class Store:
    def __init__(self):
        self.products: list[Product] = []
        self.customers: list[Customer]  = []


# Завантаження товарів з файлу
products: list[Product] = []

with open("products.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(";")

        name = data[0]
        category = data[1]
        price = float(data[2])
        stock = int(data[3])

        product = Product(name, category, price, stock)
        products.append(product)


# Завантаження клієнтів з файлу
customers: list[Customer] = []

with open("customers.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(";")

        name = data[0]
        email = data[1]

        customer = Customer(name, email)
        customers.append(customer)


# Створення магазину
store = Store()

store.products = products
store.customers = customers


# Створення замовлення для клієнта
for customer in store.customers:
    if customer.name == "Олег":
        order = Order()

        product = store.products[0]
        order.add_product(product, 1)
       

        product = store.products[1]
        order.add_product(product, 2)
        

        order.calculate_total()
        customer.add_order(order)

        print(f"Клієнт: {customer.name}")
        print(f"Email: {customer.email}")
        print(f"Сума замовлення: {order.total_amount}")

        print("Товари в замовленні:")
        for product, quantity in order.products:
            print(f"- {product.name}: {quantity} шт.")

        print("Залишок на складі:")
        for product in store.products:
            print(f"- {product.name}: {product.stock} шт.")