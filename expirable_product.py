from product import Product

class ExpirableProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, expired: bool):
        super().__init__(name, price, quantity)
        self._expired = expired

    def is_expired(self):
        return self._expired