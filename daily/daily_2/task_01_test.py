import pytest
import task_01

@pytest.fixture
def get_unpaid_invoices():
    return task_01.get_unpaid_invoices(task_01.invoices)

def test_list_len_1(get_unpaid_invoices):
    assert len(get_unpaid_invoices) == 1

def test_got_id_3(get_unpaid_invoices):
    assert any(invoice["id"] == 3 for invoice in get_unpaid_invoices)

def test_0_amount_invoice_ignored(get_unpaid_invoices):
    assert not any(invoice["amount"] == 0 for invoice in get_unpaid_invoices)