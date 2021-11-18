
# O(1) time | O(1) space
def validIPAddresses(string):
    if string is None or len(string) < 4:
        return []

    res = []

    for i in range(1, min(len(string), 4)):
        address = [None] * 4
        address[0] = string[:i]
        if not isValid(address[0]):
            continue

        for j in range(i + 1, min(len(string), i + 4)):
            address[1] = string[i:j]
            if not isValid(address[1]):
                continue

            for k in range(j + 1, min(len(string), j + 4)):
                address[2] = string[j:k]
                address[3] = string[k:]

                if isValid(address[2]) and isValid(address[3]):
                    res.append('.'.join(address))

    return res


def isValid(data):
    try:
        num = int(data)
        if 0 > num or num > 255:
            return False
        return str(num) == data
    except:
        return False


if __name__ == '__main__':
    input = "1921680"
    expected = [
        "1.9.216.80",
        "1.92.16.80",
        "1.92.168.0",
        "19.2.16.80",
        "19.2.168.0",
        "19.21.6.80",
        "19.21.68.0",
        "19.216.8.0",
        "192.1.6.80",
        "192.1.68.0",
        "192.16.8.0",
    ]
    actual = validIPAddresses(input)
    print(actual)
    assert actual == expected
