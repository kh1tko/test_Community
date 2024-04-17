import pytest


def test_1():
    assert True


@pytest.mark.smoke
def test_2():
    assert True


def test_3():
    assert True


@pytest.mark.smoke
@pytest.mark.retest
def test_4():
    assert True


def test_5():
    assert True


@pytest.mark.smoke
def test_6():
    assert True


def test_7():
    assert True


@pytest.mark.regression
def test_8():
    assert True


def test_9():
    assert True


@pytest.mark.smoke
def test_10():
    assert True
