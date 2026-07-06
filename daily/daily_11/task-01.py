products = [
    {"name": "apple", "category": "food", "price": 1.5},
    {"name": "steak", "category": "food", "price": 12.99},
    {"name": "pen", "category": "office", "price": 0.99},
    {"name": "laptop", "category": "office", "price": 999},
    {"name": "phone", "category": "electronics", "price": 599},
    {"name": "headphones", "category": "electronics", "price": 199},
]

def get_most_expensive_by_category(products: list) -> str:
    top_by_category = {}
    for p in products:
        if p["category"] not in top_by_category:
            top_by_category[p["category"]] = []
        top_by_category[p["category"]].append(p)
    
    result = {}
    for category, items in top_by_category.items():
        best = max(items, key=lambda x: x["price"])
        result[category] = best["name"]

    return result

print(get_most_expensive_by_category(products))