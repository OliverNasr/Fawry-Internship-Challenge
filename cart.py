from product import Product

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product: Product, quantity: int):
        if quantity > product.quantity:
            raise ValueError("Requested quantity exceeds stock")
        self.items.append(CartItem(product, quantity))

    def is_empty(self):
        return len(self.items) == 0

    def total(self):
        return sum(item.subtotal() for item in self.items)
