import pytest


@pytest.fixture
def client():
    print("-->Connection<--")
    value = 42
    yield value
    print("--> End of Connection<--")


@pytest.fixture
def numbers():
    tuple_numbers = (1, 2, 3, 4, 5)
    yield tuple_numbers


def test_addition(numbers):
    assert sum(numbers) == 15


def test_found(numbers):
    assert 5 in numbers
