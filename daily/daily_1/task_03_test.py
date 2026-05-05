import pytest
import task_03

def test_uid_1():
    assert task_03.get_user_from_db(1)["name"] == "Alice"

def test_uid_2():
    assert task_03.get_user_from_db(2)["name"] == "Bob"

def test_uid_99():
    with pytest.raises(KeyError):
         task_03.get_user_from_db(99)