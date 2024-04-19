# Напишіть функцію power(base, exponent), яка підносить число base до степеня exponent.
# Параметризуйте тести для цієї функції з використанням pytest.param для різних пар чисел

import pytest


def power(base, exponent):
    return base ** exponent


@pytest.mark.parametrize('base, exponent, expected', [
    (2, 4, 16),
    (3, 3, 27),
    (-2, -4, 0.0625)
])
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected
