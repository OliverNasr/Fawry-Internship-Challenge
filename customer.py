class Customer:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def deduct(self, amount: float):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount