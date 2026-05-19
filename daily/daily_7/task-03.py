transactions = [
    {"id": 1, "amount": 150, "category": "food", "approved": True},
    {"id": 2, "amount": 80, "category": "transport", "approved": False},
    {"id": 3, "amount": 200, "category": "food", "approved": True},
    {"id": 4, "amount": 50, "category": "transport", "approved": True},
    {"id": 5, "amount": 300, "category": "food", "approved": False},
]

# {
#     "food": 350,
#     "transport": 50
# }

def get_approved_total_by_category(transactions: dict) -> dict:
    transactions_by_category = {}
    for t in transactions:
        if t["approved"] == True:
            if t["category"] not in transactions_by_category:
                transactions_by_category[t["category"]] = t["amount"]
            else:
                transactions_by_category[t["category"]] += t["amount"]
    return transactions_by_category

print(get_approved_total_by_category(transactions))