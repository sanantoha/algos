from arrays.move_element_to_end import move_element_to_end


def test_move_element_to_end():
    res = move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    print(res)

    assert res == [3, 1, 4, 2, 2, 2, 2, 2]