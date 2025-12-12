from arrays.two_number_sum import two_number_sum2, two_number_sum, two_number_sum1

arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
exp = [-1, 11]

def test_two_number_sum():
    res = two_number_sum(arr, target)
    assert exp == sorted(res)

def test_two_number_sum1():
    res = two_number_sum1(arr, target)
    assert exp == sorted(res)

def test_two_number_sum2():
    res = two_number_sum2(arr, target)
    assert exp == sorted(res)