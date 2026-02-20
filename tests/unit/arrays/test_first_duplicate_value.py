import pytest

from arrays.first_duplicate_value import first_duplicate_value0, first_duplicate_value


TEST_CASES = [
    ([2, 1, 5, 2, 3, 3, 4], 2)
]


@pytest.mark.parametrize("array, exp", TEST_CASES)
def test_first_duplicate_value_case1(array, exp):
    assert first_duplicate_value0(array) == exp


@pytest.mark.parametrize("array, exp", TEST_CASES)
def test_first_duplicate_value_case2(array, exp):
    assert first_duplicate_value(array) == exp