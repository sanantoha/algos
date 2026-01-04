
# O(log(n)) time | O(log(n)) space
def calc_pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return pow(1/x, -n)

    if n % 2 == 0:
        y = pow(x, n // 2)
        return y * y
    else:
        return x * pow(x, n - 1)


if __name__ == '__main__':
    assert calc_pow(4, 2) == 16
    assert calc_pow(2, 4) == 16
    assert calc_pow(2.0, -2) == 0.25
    assert calc_pow(2.1, 3) == 9.261000000000001
