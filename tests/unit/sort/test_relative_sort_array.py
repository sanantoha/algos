import pytest

from sort.relative_sort_array import relative_sort_array, relative_sort_array_hashmap, relative_sort_array_counting_sort

TEST_CASE = [
    ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6], [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]),
    ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44])
]


@pytest.mark.parametrize("arr1, arr2, exp", TEST_CASE)
def test_relative_sort_array(arr1, arr2, exp):
    assert relative_sort_array(arr1, arr2) == exp


@pytest.mark.parametrize("arr1, arr2, exp", TEST_CASE)
def test_relative_sort_array_hashmap(arr1, arr2, exp):
    assert relative_sort_array_hashmap(arr1, arr2) == exp


@pytest.mark.parametrize("arr1, arr2, exp", TEST_CASE)
def test_relative_sort_array_counting_sort(arr1, arr2, exp):
    assert relative_sort_array_counting_sort(arr1, arr2) == exp