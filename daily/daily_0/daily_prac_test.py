import pytest
import daily.daily_0.daily_prac as daily_prac

@pytest.fixture
def get_userslol():
    return daily_prac.userslol.copy()

def test_valid_user():
    """Valid user"""
    assert daily_prac.is_valid_user(daily_prac.userslol)

def test_missing_username(get_userslol):
    """Missing username"""
    del get_userslol["username"]
    assert not daily_prac.is_valid_user(get_userslol)

def test_empty_username(get_userslol):
    """Empty username"""
    get_userslol["username"] = ""
    assert not daily_prac.is_valid_user(get_userslol)

def test_age_17(get_userslol):
    """Age 17"""
    get_userslol["age"] = 17
    assert not daily_prac.is_valid_user(get_userslol)

def test_age_18(get_userslol):
    """Age 18"""
    get_userslol["age"] = 18
    assert daily_prac.is_valid_user(get_userslol)