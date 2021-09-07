
# O(n) time | O(n) space
def get_nth_fib(n):
    return _get_nth_fib(n - 1, 0, 1)


def _get_nth_fib(n, x, y):
    if n <= 0:
        return x
    else:
        return _get_nth_fib(n - 1, y, x + y)


# O(n) time | O(1) space
def get_nth_fib_iter(n):
    k = n - 1
    x = 0
    y = 1
    while k > 0:
        x, y = y, x + y
        k -= 1

    return x


if __name__ == '__main__':
    for i in range(1, 10):
        print(str(i) + "=" + str(get_nth_fib(i)))

    print("===================================")

    for i in range(1, 10):
        print(str(i) + "=" + str(get_nth_fib_iter(i)))
