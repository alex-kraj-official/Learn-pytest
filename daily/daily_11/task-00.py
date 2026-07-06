products = [
    {"name": "apple", "price": 1.5},
    {"name": "laptop", "price": 999},
    {"name": "pen", "price": 0.99},
    {"name": "phone", "price": 599},
    {"name": "notebook", "price": 4.99},
]

def filter_by_min_price(products: list, min_price: float) -> list:
    return [p for p in products if p["price"] >= min_price]

print(filter_by_min_price(products, 5))