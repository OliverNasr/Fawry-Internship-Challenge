from expirable_product import ExpirableProduct
from shippable_product import ShippableProduct
from customer import Customer
from cart import Cart
from shipping_service import ShippingService
from product import Product
from expirable_shippable import ExpirableShippableProduct

print("Welcome to the Fawry E-Commerce System\n")

name = input("Enter customer name: ")
balance = float(input("Enter customer balance: "))
customer = Customer(name, balance)

print("\nDefine products (type 'done' as name to finish):")
products = [    
    ShippableProduct("Cheese", 100, 5, 200),
    ShippableProduct("Biscuits", 150, 3, 700),
    ExpirableProduct("Oranges", 50, 10, False),
    ShippableProduct("TV", 1000, 2, 8000)]

while True:
    pname = input("Product name: ")
    if pname.lower() == 'done':
        break
    pprice = float(input("Price: "))
    pquantity = int(input("Available quantity: "))

    expirable = input("Is this product expirable after a certain amount of time? (yes/no): ").lower() == 'yes'
    expired = False
    if expirable:
        expired = False  # automatically set since it will expire later

    shippable = input("Is this product shippable? (yes/no): ").lower() == 'yes'
    weight = 0.0
    if shippable:
        weight = float(input("Enter weight in grams: "))

    if expirable and shippable:
        product = ShippableProduct(pname, pprice, pquantity, weight)
        product._expired = expired  # patch: product is not yet expired
    elif expirable:
        product = ExpirableProduct(pname, pprice, pquantity, expired)
    elif shippable:
        product = ShippableProduct(pname, pprice, pquantity, weight)
    else:
        from product import Product
        product = Product(pname, pprice, pquantity)

    products.append(product)

cart = Cart()
print("\nAdd products to cart (type 'done' to finish):")
while True:
    for idx, prod in enumerate(products):
        print(f"[{idx}] {prod.name} - {prod.price} EGP - Stock: {prod.quantity}")
    choice = input("Select product number: ")
    if choice.lower() == 'done':
        break
    try:
        idx = int(choice)
        quantity = int(input("Quantity to add: "))
        cart.add(products[idx], quantity)
    except Exception as e:
        print("Error:", e)

if cart.is_empty():
    print("Cart is empty")
else:
    shipping_items = []
    subtotal = 0.0

    for item in cart.items:
        if item.product.is_expired():
            print(f"{item.product.name} is expired.")
            exit()
        if item.product.quantity < item.quantity:
            print(f"{item.product.name} is out of stock.")
            exit()

        item.product.reduce_quantity(item.quantity)
        subtotal += item.subtotal()

        if item.product.is_shippable():
            shipping_items.append({
                'name': item.product.name,
                'weight': item.product.get_weight(),
                'quantity': item.quantity
            })

    shipping_service = ShippingService()
    shipping_cost = shipping_service.ship(shipping_items) if shipping_items else 0

    total_amount = subtotal + shipping_cost
    try:
        customer.deduct(total_amount)
    except ValueError as e:
        print(e)
        exit()

    print("** Checkout receipt **")
    for item in cart.items:
        print(f"{item.quantity}x {item.product.name}\t{item.subtotal()}")
    print("----------------------")
    print(f"Subtotal\t{subtotal}")
    print(f"Shipping\t{shipping_cost}")
    print(f"Amount\t{total_amount}")
    print(f"Balance\t{customer.balance}")
    print("Thank you for shopping with us!")