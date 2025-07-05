from abc import ABC

class Product(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def reduce_quantity(self, amount: int):
        if amount > self._quantity:
            raise ValueError("Not enough stock.")
        self._quantity -= amount

    def is_expired(self):
        return False

    def is_shippable(self):
        return False

    def get_weight(self):
        return 0.0

    def __str__(self):
        return f"{self._name}: {self._price} EGP ({self._quantity} left)"
