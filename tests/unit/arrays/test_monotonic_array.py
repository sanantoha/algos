from arrays.monotonic_array import monotonic_array


def test_monotonic_array():
    assert monotonic_array([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])