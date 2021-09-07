
# O(n) time | O(1) space
def find_three_largest_numbers(array):
    res = [float('-inf')] * 3

    for num in array:
        if res[2] < num:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = num
        elif res[1] < num:
            res[0] = res[1]
            res[1] = num
        elif res[0] < num:
            res[0] = num

    return res


# O(n) time | O(1) space
def find_three_largest_numbers1(array):
    three_largest = [float('-inf')] * 3

    for num in array:
        upload_largest(three_largest, num)
    return three_largest


def upload_largest(three_largest, num):
    if num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


if __name__ == '__main__':
    print(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541])
    print(find_three_largest_numbers1([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541])

