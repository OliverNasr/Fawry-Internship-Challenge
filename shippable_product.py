from product import Product

class ShippableProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, weight: float):
        super().__init__(name, price, quantity)
        self._weight = weight

    def is_shippable(self):
        return True

    def get_weight(self):
        return self._weight