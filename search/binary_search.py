
# O(log(n)) time | O(1) space
def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
        else:
            return mid

    return -(left + 1)


if __name__ == '__main__':
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
    print(binary_search(array, 140))
