products = [
    {"name": "apple", "category": "fruit"},
    {"name": "banana", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "broccoli", "category": "vegetable"},
    {"name": "milk", "category": "dairy"},
    {"name": "apple", "category": "fruit"},
]

# {"fruit": 3, "vegetable": 2, "dairy": 1}

def count_by_category(products: dict) -> dict:
    categories_count = {}
    for p in products:
        if p["category"] not in categories_count:
            categories_count[p["category"]] = 0
        categories_count[p["category"]] += 1
    return categories_count

print (count_by_category(products))