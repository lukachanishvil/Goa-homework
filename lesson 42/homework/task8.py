
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 1200,
    "stock": 5
}

price = product.get("price")
print(f"Price: {price}")

discount = product.get("discount", "No discount available")
print(f"Discount: {discount}")
