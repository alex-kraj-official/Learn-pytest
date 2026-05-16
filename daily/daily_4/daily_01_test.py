import pytest
import daily_01

def test_empty_list():
    assert daily_01.summarize_invoices([]) == {
        "total_count": 0,
        "paid_count": 0,
        "unpaid_count": 0,
        "unpaid_total": 0
        }

def test_2():
    test_inv = daily_01.invoices.copy()
    test_inv.append({"id": 5, "amount": 0, "paid": False})
    assert daily_01.summarize_invoices(test_inv)["unpaid_total"] == 500

def test_3():
    test_inv2 = daily_01.invoices.copy()
    test_inv2.append({"id": 5, "amount": 0, "paid": True})
    assert daily_01.summarize_invoices(test_inv2)["paid_count"] == 3

def test_4():
    test_inv2 = daily_01.invoices.copy()
    test_inv2.append({"id": 15, "amount": 0, "paid": True})
    assert daily_01.summarize_invoices(test_inv2)["paid_count"] == 3 and daily_01.summarize_invoices(test_inv2)["total_count"] == 5