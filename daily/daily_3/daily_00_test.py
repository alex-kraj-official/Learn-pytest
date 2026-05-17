import pytest
import daily_00

def test_id_3():
    assert daily_00.find_most_expensive(daily_00.invoices) == 3

def test_all_paid_None():
    all_paid = [
        {"id": 1, "amount": 150, "paid": True},
        {"id": 2, "amount": 200, "paid": True},
    ]
    for i in all_paid:
        i["paid"] = True
    assert daily_00.find_most_expensive(all_paid) == None

def test_empty_list_None():
    assert daily_00.find_most_expensive([]) is None