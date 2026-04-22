import pytest

from sort.insertion_sort import insertion_sort, insertion_sort2

TEST_CASES = [
    ([9, 8, 1, 5, 6, 7, 8, 3, 9, 7, 5, 3], [1, 3, 3, 5, 5, 6, 7, 7, 8, 8, 9, 9]),
]


@pytest.mark.parametrize("arr, exp", TEST_CASES)
def test_insertion_sort(arr, exp):
    assert insertion_sort(arr) == exp



@pytest.mark.parametrize("arr, exp", TEST_CASES)
def test_insertion_sort2(arr, exp):
    assert insertion_sort2(arr) == exp