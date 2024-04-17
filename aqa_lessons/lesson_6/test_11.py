import pytest


@pytest.mark.order(3)
def test_logout():
    assert True


@pytest.mark.order(1)
def test_login():
    assert True


@pytest.mark.order(2)
def test_search():
    assert True
