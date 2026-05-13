import pytest
import task_00

def test_list_with_3_elements():
    assert len(task_00.get_errors(task_00.errors)) == 3

def test_no_200_code():
    got_200_code = False
    for error in task_00.get_errors(task_00.errors):
        if error["code"] == 200:
            got_200_code = True

    assert got_200_code == False

def test_got_404_code():
    got_404_code = False
    for error in task_00.get_errors(task_00.errors):
        if error["code"] == 404:
            got_404_code = True

    assert got_404_code == True

def test_no_200_code_upg():
    errors = task_00.get_errors(task_00.errors)
    assert not any(error["code"] == 200 for error in errors)

def test_got_404_code_upg():
    errors = task_00.get_errors(task_00.errors)
    assert any(error["code"] == 404 for error in errors)