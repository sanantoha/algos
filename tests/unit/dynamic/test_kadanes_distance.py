import pytest

from dynamic.kadanes_distance import kadanes_distance, kadanes_distance1

TEST_CASES = [
    ([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4], 19),
]

@pytest.mark.parametrize("arr, exp", TEST_CASES)
def test_kadanes_distance(arr, exp):
    assert kadanes_distance(arr) == exp


@pytest.mark.parametrize("arr, exp", TEST_CASES)
def test_kadanes_distance1(arr, exp):
    assert kadanes_distance1(arr) == exp