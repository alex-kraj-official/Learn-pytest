invoices = [
    {"id": 1, "amount": 150, "paid": True},
    {"id": 2, "amount": 200, "paid": False},
    {"id": 3, "amount": 300, "paid": False},
]

def get_invoice_by_id(invoices: list, invoice_id: int) -> dict:
    searched_invoice = {}
    for invoice in invoices:
        if invoice_id is invoice["id"]:
            searched_invoice = invoice
            return searched_invoice
    raise ValueError("Invoice not found: 99")

# print(get_invoice_by_id(invoices, 4))