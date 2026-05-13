invoices = [
    {"id": 1, "amount": 150, "paid": True},
    {"id": 2, "amount": 200, "paid": False},
    {"id": 3, "amount": 300, "paid": False},
    {"id": 4, "amount": 50, "paid": True},
]

def calculate_total(invoices: list) -> int:
    return sum(invoice["amount"] for invoice in invoices if not invoice["paid"])

print(calculate_total(invoices))