transactions = [
    {"id": 1, "category": "food", "amount": 50},
    {"id": 2, "category": "transport", "amount": 30},
    {"id": 3, "category": "food", "amount": 80},
    {"id": 4, "category": "transport", "amount": 20},
    {"id": 5, "category": "entertainment", "amount": 100},
]

# {
#     "food": [50, 80],
#     "transport": [30, 20],
#     "entertainment": [100]
# }


def group_by_category(transactions: list) -> dict:
    food = sum(t["amount"] for t in transactions if t["category"] == "food")
    transport = sum(t["amount"] for t in transactions if t["category"] == "transport")
    entertainment = sum(t["amount"] for t in transactions if t["category"] == "entertainment")
    categories = [
        {"food": food},
        {"transport": transport},
        {"entertainment": entertainment}
    ]
    return categories

print(group_by_category(transactions))
