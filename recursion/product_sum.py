
def product_sum(array, level=1):
    total_sum = 0

    for n in array:
        if type(n) is list:
            total_sum += product_sum(n, level + 1)
        else:
            total_sum += n
    return total_sum * level


if __name__ == '__main__':
    print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12)
