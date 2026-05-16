import pytest
import daily_00

def test_id_1():
    assert daily_00.get_invoice_by_id(daily_00.invoices, 1) == {"id": 1, "amount": 150, "paid": True}

def test_id_3():
    assert daily_00.get_invoice_by_id(daily_00.invoices, 3)["paid"] is False

def test_id_99():
    with pytest.raises(ValueError):
        assert daily_00.get_invoice_by_id(daily_00.invoices, 99)

def test_id_99_2():
    with pytest.raises(ValueError, match="99"):
        assert daily_00.get_invoice_by_id(daily_00.invoices, 99)