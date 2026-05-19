transactions = [
    {"id": 1, "amount": 150, "category": "food", "approved": True},
    {"id": 2, "amount": 80, "category": "transport", "approved": False},
    {"id": 3, "amount": 200, "category": "food", "approved": True},
    {"id": 4, "amount": 50, "category": "transport", "approved": True},
    {"id": 5, "amount": 300, "category": "food", "approved": False},
]

# {
#     "total_count": 5,
#     "approved_count": 3,
#     "rejected_count": 2,
#     "approved_total": 400,
#     "most_expensive_approved": 200
# }

def summarize_transactions(transactions: list) -> dict:
    total_count = len(transactions)
    approved_count = sum(1 for t in transactions if t["approved"])
    rejected_count = sum(1 for t in transactions if not t["approved"])
    approved_total = sum(t["amount"] for t in transactions if t["approved"])
    most_expensive_approved = max(t["amount"] for t in transactions if t["approved"])
    
    summarized_transactions = {
        "total_count": total_count,
        "approved_count": approved_count,
        "rejected_count": rejected_count,
        "approved_total": approved_total,
        "most_expensive_approved": most_expensive_approved
    }

    return summarized_transactions

print(summarize_transactions(transactions))