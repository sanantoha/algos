
# O(n) time | O(n) space
def first_duplicate_value0(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1


# O(n) time | O(1) space
def first_duplicate_value(array):
    if array is None or len(array) == 0:
        return -1

    for i in range(len(array)):
        val = abs(array[i])
        if array[val - 1] < 0:
            return val
        array[val - 1] *= -1

    return -1


if __name__ == '__main__':
    array = [2, 1, 5, 2, 3, 3, 4]
    print(first_duplicate_value0(array))
    print(first_duplicate_value(array))
