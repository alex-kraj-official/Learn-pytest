invoices = [
    {"id": 1, "amount": 150, "paid": True},
    {"id": 2, "amount": 200, "paid": False},
    {"id": 3, "amount": 300, "paid": False},
    {"id": 4, "amount": 50, "paid": True},
]

def find_most_expensive(invoices: list) -> int:
    unpaid = [i for i in invoices if not i["paid"]]
    if not unpaid: return None
    max_unpaid = max(unpaid, key= lambda i: i["amount"])
    return (max_unpaid["id"])

print(find_most_expensive(invoices))