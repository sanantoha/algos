
# O(n * log(n)) time | O(n) space
def sorted_squared_array(array):
    res = []
    if array is None or len(array) == 0:
        return res

    for num in array:
        res.append(num * num)

    return sorted(res)


# O(n) time | O(n) space
def sorted_squared_array1(array):
    res = [0 for _ in array]
    if array is None or len(array) == 0:
        return res

    smallest_idx = 0
    largest_idx = len(array) - 1

    for i in reversed(range(len(array))):
        smallest_val = array[smallest_idx]
        largest_val = array[largest_idx]

        if abs(smallest_val) > abs(largest_val):
            res[i] = smallest_val * smallest_val
            smallest_idx += 1
        else:
            res[i] = largest_val * largest_val
            largest_idx -= 1

    return res


if __name__ == '__main__':
    print(sorted_squared_array1([-3, 1, 2, 3, 5, 6, 8, 9]))
