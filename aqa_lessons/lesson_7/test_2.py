import pytest


def sum_list(numbers: list) -> int | float:
    return sum(numbers)


@pytest.mark.parametrize('numbers, expected_result', [
    pytest.param([1, 2, 3, 4, 5], 15, id='Positive test'),
    pytest.param([], 0, id='Empty list'),
    pytest.param([99, 98, 97, 96, 95], 485, id='Positive test_2')
])
def test_sum_list(numbers, expected_result):
    assert sum_list(numbers) == expected_result
