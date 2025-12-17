from tree.same_bsts import sameBsts, sameBsts1
import pytest

TEST_CASES = [
    ([10, 15, 8, 12, 94, 81, 5, 2, 11],
     [10, 8, 5, 15, 2, 12, 11, 94, 81],
     True),
    ([1], [1], True),
    ([], [], True),
    ([1, 2], [1, 3], False),
]


@pytest.mark.parametrize("arr1, arr2, expected", TEST_CASES)
def test_sameBsts(arr1, arr2, expected):
    assert sameBsts(arr1, arr2) == expected



@pytest.mark.parametrize("arr1, arr2, expected", TEST_CASES)
def test_sameBsts1(arr1, arr2, expected):
    assert sameBsts1(arr1, arr2) == expected