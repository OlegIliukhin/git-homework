# =========================
# Класс Product (Товар)
# =========================

class Product:
    def __init__(self, name: str, category: str, price: float, quantity: int):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price: float):
        self.price = new_price

    def change_quantity(self, new_quantity: int):
        self.quantity = new_quantity


# =========================
# Класс Order (Замовлення)
# =========================

class Order:
    def __init__(self):
        self.products = []  # список (product, quantity)
        self.total_sum = 0

    def add_product(self, product: Product, quantity: int):
        if product.quantity >= quantity:
            self.products.append((product, quantity))
            product.change_quantity(product.quantity - quantity)
        else:
            print("Недостатньо товару на складі")

    def calculate_total(self):
        self.total_sum = 0
        for product, quantity in self.products:
            self.total_sum += product.price * quantity
        return self.total_sum
# =========================
# Класс Customer (Клієнт)
# =========================

class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)


# =========================
# Тестування
# =========================

if __name__ == "__main__":
    toy = Product("Мишка", "м'яка іграшка", 300, 10)
    lego = Product("Лего", "конструктор", 800, 5)

    order = Order()
    order.add_product(toy, 2)
    order.add_product(lego, 1)

    customer = Customer("Олег", "oleg@gmail.com")
    customer.add_order(order)

    print("Клієнт:", customer.name)
    print("Email:", customer.email)
    print("Сума замовлення:", order.calculate_total())
    print("Залишок мишок:", toy.quantity)
    print("Залишок лего:", lego.quantity)