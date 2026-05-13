invoices = [
    {"id": 1, "amount": 150, "paid": True},
    {"id": 2, "amount": 0, "paid": False},
    {"id": 3, "amount": 300, "paid": False},
    {"id": 4, "amount": 50, "paid": True},
]

def get_unpaid_invoices(invoices: list) -> list:
    unpaid_invoices = []
    for invoice in invoices:
        if (invoice["paid"] == False) and (invoice["amount"] > 0):
            unpaid_invoices.append(invoice)
    return unpaid_invoices

print(get_unpaid_invoices(invoices))