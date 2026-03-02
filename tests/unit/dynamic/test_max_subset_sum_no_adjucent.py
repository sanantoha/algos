from dynamic.max_subset_sum_no_adjucent import max_subset_sum_no_adjucent, max_subset_sum_no_adjucent1

import pytest


TEST_CASES = [
    ([75, 105, 120, 75, 90, 135], 330)
]


@pytest.mark.parametrize("arr, exp", TEST_CASES)
def test_max_subset_sum_no_adjucent_case1(arr, exp):
    assert max_subset_sum_no_adjucent(arr) == exp


@pytest.mark.parametrize("arr, exp", TEST_CASES)
def test_max_subset_sum_no_adjucent_case2(arr, exp):
    assert max_subset_sum_no_adjucent1(arr) == exp