
# O(n ^ 2) time | O(1) space
def insert_sort(arr):

    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        for j in range(i - 1, -2, -1):
            if arr[j] < value:
                break
            arr[j + 1] = arr[j]
        arr[j + 1] = value

    return arr


# O(n ^ 2) time | O(1) space
def insert_sort2(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1

    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    xs = [9, 8, 1, 5, 6, 7, 8, 3, 9, 7, 5, 3]
    # xs = [5,2,4,1]
    print(insert_sort(xs))
    print(insert_sort2(xs))
