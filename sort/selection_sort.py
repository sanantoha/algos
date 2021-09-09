# best/average/worst
# O(n ^ 2) time | O(1) space
def selection_sort(arr):

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        if i != min_idx:
            swap(arr, i, min_idx)

    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [9, 8, 1, 5, 6, 7, 8, 3, 9, 7, 5, 3]
    print(selection_sort(arr))
