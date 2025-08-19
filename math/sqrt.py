
# O(log(n)) time | O(1) space
def sqrt(n):
    l = 0
    r = n

    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid <= n:
            l = mid + 1
        else:
            r = mid - 1

    return l - 1


if __name__ == '__main__':
    assert sqrt(4) == 2
    assert sqrt(5) == 2
    assert sqrt(6) == 2
    assert sqrt(7) == 2
    assert sqrt(8) == 2
    assert sqrt(16) == 4
