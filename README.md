# 🛒 Fawry E-Commerce System (Internship Challenge 3)

A modular, object-oriented e-commerce system built in Python as part of the **Fawry Rise Journey Full Stack Internship Challenge**.

## 🚀 Project Overview

This project simulates an e-commerce platform with features like:
- Custom and default product management
- Product types: expirable, shippable, or both
- Customer balance management and cart system
- Shipping cost calculation
- Checkout with detailed receipts

It demonstrates core object-oriented principles and simulates realistic e-commerce checkout logic.

## 📦 Features

- Add customers with specific balances  
- Add predefined and user-defined products  
- Support for:
  - Expirable Products (e.g., Scratch Cards)
  - Shippable Products (e.g., Cheese, TV)
  - Expirable + Shippable Products (e.g., Fresh Milk)
- Add items to cart with quantity checks  
- Validation for:
  - Expired items
  - Empty cart
  - Insufficient balance
  - Out of stock items
- Dynamic checkout summary with shipping details

## 🧠 OOP Concepts Demonstrated

- **Encapsulation** – Controlled product access via properties  
- **Inheritance** – Base and specialized product classes  
- **Polymorphism** – Shipping behavior via shared interface  
- **Abstraction** – Use of abstract base `Product`  
- **Modular Design** – Separated class responsibilities

## 📂 Project Structure

# 📄 main_app.py

A fully interactive **command-line app** that allows users to:

1. Enter their name and balance  
2. Use default or custom products (define name, type, price, quantity)  
3. Add items to a cart  
4. Checkout with full validation and output

# ✅ test_app.py

Runs a series of **test cases** to ensure the system is working as intended:

- ✅ Successful checkout scenario  
- ❌ Insufficient balance triggers error  
- ⚠️ Expired product is caught before checkout  
- 🛒 Empty cart check  
- 🏪 Out of stock protection  
- 🧪 Combined expirable and shippable product test  
