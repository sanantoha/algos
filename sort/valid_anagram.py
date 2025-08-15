
# O(s + t) time | O(d) space - unique chars in s and t
def isAnagram(s: str, t: str):
    if not s or not t:
        return False

    if len(s) != len(t):
        return False

    d = {}
    for c in s:
        cnt = d.get(c, 0)
        d[c] = cnt + 1

    for c in t:
        cnt = d.get(c, 0)
        d[c] = cnt - 1
        if d[c] < 0:
            return False

    for _, v in d.items():
        if v != 0:
            return False

    return True


if __name__ == '__main__':
    res = isAnagram("anagram", "nagaram")
    print(res)
    assert res

    res = isAnagram("rat", "cat")
    print(not res)
    assert not res
