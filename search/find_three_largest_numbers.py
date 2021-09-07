
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


if __name__ == '__main__':
    print(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541])
