import pytest
import task_02

@pytest.fixture
def get_total():
    return task_02.calculate_total(task_02.invoices)

def test_sum_is_500(get_total):
    assert get_total == 500

def test_eone_paid_then_sum_is_0(get_total):
    all_paid = [
        {"id": 1, "amount": 150, "paid": True},
        {"id": 2, "amount": 200, "paid": True},
    ]
    assert task_02.calculate_total(all_paid) == 0

def test_empty_list_then_sum_is_0():
    assert task_02.calculate_total([]) == 0