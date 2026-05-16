invoices = [
    {"id": 1, "amount": 150, "paid": True},
    {"id": 2, "amount": 200, "paid": False},
    {"id": 3, "amount": 300, "paid": False},
    {"id": 4, "amount": 50, "paid": True},
]

def summarize_invoices(invoices: list) -> dict:
    total_count = len(invoices)
    paid_count = sum(1 for i in invoices if i["paid"])
    unpaid_count = sum(1 for i in invoices if not i["paid"])
    unpaid_total = sum(i["amount"] for i in invoices if not i["paid"])
    summarized = {
        "total_count": total_count,
        "paid_count": paid_count,
        "unpaid_count": unpaid_count,
        "unpaid_total": unpaid_total
    }
    return summarized

print(summarize_invoices(invoices))