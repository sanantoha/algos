
# O(n) time | O(n) space
def bestDigits(number, numDigits):
    stack = []

    for digit in number:
        while numDigits > 0 and stack and digit > stack[-1]:
            numDigits -= 1
            stack.pop()

        stack.append(digit)

    while numDigits > 0:
        numDigits -= 1
        stack.pop()

    return "".join(stack)


if __name__ == '__main__':
    number = "462839"
    numDigits = 2

    actual = bestDigits(number, numDigits)
    print(actual)
    assert actual == "6839"

    actual = bestDigits("648239", numDigits)
    print(actual)
    assert actual == "8239"

    actual = bestDigits("988762", numDigits)
    print(actual)
    assert actual == "9887"