
# O(n ^ 2) time | O(1) space
def bubble_sort(arr):
    is_sorted = False
    count = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1 - count):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                is_sorted = False
        count += 1

    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
