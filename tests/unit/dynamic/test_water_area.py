import pytest

from dynamic.water_area import waterArea, waterArea1, waterArea2


TEST_CASE = [
    ([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3], 48),
]


@pytest.mark.parametrize("arr, exp", TEST_CASE)
def test_water_area(arr, exp):
    actual = waterArea(arr)
    print(actual)
    assert actual == exp


@pytest.mark.parametrize("arr, exp", TEST_CASE)
def test_water_area1(arr, exp):
    actual = waterArea1(arr)
    print(actual)
    assert actual == exp


@pytest.mark.parametrize("arr, exp", TEST_CASE)
def test_water_area2(arr, exp):
    actual = waterArea2(arr)
    print(actual)
    assert actual == exp