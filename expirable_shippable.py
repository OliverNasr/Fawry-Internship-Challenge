# expirable_shippable_product.py
from expirable_product import ExpirableProduct
from interfaces import IShippable

class ExpirableShippableProduct(ExpirableProduct, IShippable):
    def __init__(self, name: str, price: float, quantity: int, expired: bool, weight: float):
        super().__init__(name, price, quantity, expired)
        self._weight = weight

    def get_weight(self) -> float:
        return self._weight

    def is_shippable(self) -> bool:
        return True