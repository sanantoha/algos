
# O(n) time | O(1) space
def oneEdit(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if abs(l1 - l2) > 1:
        return False

    makeEdit = False
    idx1 = 0
    idx2 = 0

    while idx1 < l1 and idx2 < l2:
        if s1[idx1] != s2[idx2]:
            if makeEdit:
                return False

            makeEdit = True

            if l1 > l2:
                idx2 += 1
            elif l1 < l2:
                idx1 += 1
            else:
                idx1 += 1
                idx2 += 1
        else:
            idx1 += 1
            idx2 += 1

    return True


if __name__ == '__main__':
    stringOne = "hello"
    stringTwo = "helo"
    expected = True
    actual = oneEdit(stringOne, stringTwo)
    print(actual)
    assert actual == expected