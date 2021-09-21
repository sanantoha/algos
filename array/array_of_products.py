
# O(n) time | O(n) space
def array_of_products(array):
    if array is None or len(array) == 0:
        return array

    res = [1 for _ in range(len(array))]

    for i in range(1, len(array)):
        res[i] = res[i - 1] * array[i - 1]

    prev = 1
    for i in reversed(range(len(array))):
        res[i] = res[i] * prev
        prev *= array[i]

    return res


# O(n) time | O(n) space
def array_of_products1(array):
    if array is None or len(array) == 0:
        return array

    products = [1 for _ in range(len(array))]

    left_prev = 1
    for i in range(len(array)):
        products[i] = left_prev
        left_prev *= array[i]

    right_prev = 1
    for i in reversed(range(len(array))):
        products[i] *= right_prev
        right_prev *= array[i]

    return products


if __name__ == '__main__':
    print(array_of_products([1, 2, 3, 4]))
    print(array_of_products1([1, 2, 3, 4]))
