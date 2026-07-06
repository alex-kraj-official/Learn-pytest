import statistics

products = [
    {"name": "apple", "category": "food", "price": 1.5},
    {"name": "steak", "category": "food", "price": 12.99},
    {"name": "pen", "category": "office", "price": 0.99},
    {"name": "laptop", "category": "office", "price": 999},
    {"name": "phone", "category": "electronics", "price": 599},
]

# {
#     "total_count": 5,
#     "avg_price": 322.7,
#     "most_expensive": "laptop",
#     "cheapest": "pen"
# }

def summarize_products(products: list) -> dict:
    # total_count = sum([1 for p in products])
    total_count = len(products)
    avg_price = round(statistics.mean(p["price"] for p in products), 1)
    # most_expensive = [p["name"] for p in products if p["price"] == max(p["price"] for p in products)]
    most_expensive = max(products, key=lambda p: p["price"])["name"]
    # cheapest = [p["name"] for p in products if p["price"] == min(p["price"] for p in products)]
    cheapest = min(products, key=lambda p: p["price"])["name"]

    summarized_products = dict()
    summarized_products = {
        "total_count": total_count,
        "avg_price": avg_price,
        "most_expensive": most_expensive,
        "cheapest": cheapest
    }
    return summarized_products

print(summarize_products(products))