import pytest

from dynamic.numbers_of_ways_to_traverse_graph import numbers_of_ways_to_traverse_graph_rec, \
    numbers_of_ways_to_traverse_graph, numbers_of_ways_to_traverse_graph_math

TEST_CASES = [
    (4, 3, 10)
]


@pytest.mark.parametrize("width, height, exp", TEST_CASES)
def test_numbers_of_ways_to_traverse_graph_rec(width, height, exp):
    assert numbers_of_ways_to_traverse_graph_rec(width, height) == exp


@pytest.mark.parametrize("width, height, exp", TEST_CASES)
def test_numbers_of_ways_to_traverse_graph(width, height, exp):
    assert numbers_of_ways_to_traverse_graph(width, height) == exp


@pytest.mark.parametrize("width, height, exp", TEST_CASES)
def test_numbers_of_ways_to_traverse_graph_math(width, height, exp):
    assert numbers_of_ways_to_traverse_graph_math(width, height) == exp