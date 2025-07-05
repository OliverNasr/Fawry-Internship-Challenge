# test_app.py
from expirable_product import ExpirableProduct
from shippable_product import ShippableProduct
from expirable_shippable import ExpirableShippableProduct
from customer import Customer
from cart import Cart
from shipping_service import ShippingService

def print_receipt(cart, customer, shipping_cost):
    print("** Checkout receipt **")
    for item in cart.items:
        print(f"{item.quantity}x {item.product.name}\t{item.subtotal()}")
    print("----------------------")
    print(f"Subtotal\t{cart.total()}")
    print(f"Shipping\t{shipping_cost}")
    print(f"Amount\t{cart.total() + shipping_cost}")
    print(f"Balance\t{customer.balance}\n")

def test_successful_checkout():
    print("Test: Successful Checkout")
    customer = Customer("Ali", 1000)
    cart = Cart()

    cheese = ShippableProduct("Cheese", 100, 5, 200)
    biscuits = ShippableProduct("Biscuits", 150, 3, 700)
    scratch_card = ExpirableProduct("Scratch Card", 50, 10, False)

    cart.add(cheese, 2)
    cart.add(biscuits, 1)
    cart.add(scratch_card, 1)

    shipping_items = []
    subtotal = 0.0

    for item in cart.items:
        if item.product.is_expired():
            print(f"Failed: {item.product.name} is expired.")
            return
        if item.product.quantity < item.quantity:
            print(f"Failed: {item.product.name} is out of stock.")
            return
        item.product.reduce_quantity(item.quantity)
        subtotal += item.subtotal()
        if item.product.is_shippable():
            shipping_items.append({
                'name': item.product.name,
                'weight': item.product.get_weight(),
                'quantity': item.quantity
            })

    shipping_cost = ShippingService().ship(shipping_items) if shipping_items else 0
    try:
        customer.deduct(subtotal + shipping_cost)
        print_receipt(cart, customer, shipping_cost)
        print("Passed\n")
    except ValueError as e:
        print("Failed:", e)

def test_insufficient_balance():
    print("Test: Insufficient Balance")
    customer = Customer("Lina", 50)
    cart = Cart()
    card = ExpirableProduct("Scratch Card", 100, 10, False)
    try:
        cart.add(card, 1)
        customer.deduct(cart.total())
        print("Failed: Should have thrown an error.")
    except ValueError as e:
        print("Passed:", e, "\n")

def test_expired_product():
    print("Test: Expired Product")
    customer = Customer("Omar", 500)
    cart = Cart()
    expired = ExpirableProduct("Expired Biscuits", 100, 5, True)
    cart.add(expired, 1)
    for item in cart.items:
        if item.product.is_expired():
            print(f"Passed: {item.product.name} is expired.\n")
            return
    print("Failed: Product should be expired.")

def test_empty_cart():
    print("Test: Empty Cart")
    customer = Customer("Mona", 200)
    cart = Cart()
    if cart.is_empty():
        print("Passed: Cart is empty.\n")
    else:
        print("Failed: Cart should be empty.")

def test_out_of_stock():
    print("Test: Out of Stock")
    cart = Cart()
    limited = ExpirableProduct("Scratch Card", 50, 2, False)
    try:
        cart.add(limited, 5)
        print("Failed: Should have raised stock error.")
    except ValueError as e:
        print("Passed:", e, "\n")

def test_expirable_shippable():
    print("Test: Expirable and Shippable Product")
    customer = Customer("Salma", 500)
    cart = Cart()
    combo = ExpirableShippableProduct("Fresh Milk", 80, 3, False, 1000)
    cart.add(combo, 2)
    subtotal = cart.total()
    combo.reduce_quantity(2)
    shipping_items = [{
        'name': combo.name,
        'weight': combo.get_weight(),
        'quantity': 2
    }]
    shipping_cost = ShippingService().ship(shipping_items)
    try:
        customer.deduct(subtotal + shipping_cost)
        print_receipt(cart, customer, shipping_cost)
        print("Passed\n")
    except ValueError as e:
        print("Failed:", e)

# Run all tests
test_successful_checkout()
test_insufficient_balance()
test_expired_product()
test_empty_cart()
test_out_of_stock()
test_expirable_shippable()