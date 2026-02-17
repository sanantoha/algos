
import pytest

from sort.three_number_sort import threeNumberSort1, threeNumberSort

TEST_CASE = [
    ([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1], [0, 0, 0, 1, 1, 1, -1, -1]),
]


@pytest.mark.parametrize("array, order, expected", TEST_CASE)
def test_tree_number_sort_case1(array, order, expected):
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    expected = [0, 0, 0, 1, 1, 1, -1, -1]

    actual = threeNumberSort(array, order)
    print(actual)
    assert actual == expected


@pytest.mark.parametrize("array, order, expected", TEST_CASE)
def test_tree_number_sort_case2(array, order, expected):
    actual = threeNumberSort1(array, order)
    print(actual)
    assert actual == expected