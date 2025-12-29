from sort.bubble_sort import bubble_sort


def test_bubble_sort():
    assert bubble_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]