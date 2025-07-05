class ShippingService:
    def ship(self, shippables):
        print("** Shipment notice **")
        total_weight = 0.0
        for item in shippables:
            print(f"{item['quantity']}x {item['name']}\t{item['weight'] * item['quantity']}g")
            total_weight += item['weight'] * item['quantity'] / 1000.0
        print(f"Total package weight {total_weight:.1f}kg\n")
        return total_weight * 30 # 30 EGP per kg shipping cost