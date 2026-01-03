import pytest

from search.find_three_largest_numbers import find_three_largest_numbers, find_three_largest_numbers1


params = [
    ([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7], [18, 141, 541])
]


@pytest.mark.parametrize("input, exp", params)
def test_find_three_largest_numbers(input, exp):
    assert find_three_largest_numbers(input) == exp



@pytest.mark.parametrize("input, exp", params)
def test_find_three_largest_numbers1(input, exp):
    assert find_three_largest_numbers1(input) == exp