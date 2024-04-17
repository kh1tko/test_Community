# Створіть фікстуру модуля, яка встановлює початкові дані для всіх тестів у модулі.
# Створіть функційну фікстуру, яка використовує ці дані перед кожним тестом.
# Переконайтеся, що тести використовують і обидві фікстури.

import pytest


@pytest.fixture(scope="module")
def initial_data():
    data = ['Tyma', 'Dima']
    return data


@pytest.fixture(scope="function")
def test_data(initial_data):
    data = initial_data + ['Valera']
    return data


def test_data_length(test_data):
    assert len(test_data) == 3
