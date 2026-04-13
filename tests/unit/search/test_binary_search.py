import pytest

from search.binary_search import binary_search

array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

TEST_CASES = [
    (array, 60, 5),
    (array, 61, -7),
    (array, 90, 8),
    (array, 10, 0),
    (array, 130, 12),
]


@pytest.mark.parametrize("arr, target, exp", TEST_CASES)
def test_binary_search(arr, target, exp):
    assert binary_search(arr, target) == exp