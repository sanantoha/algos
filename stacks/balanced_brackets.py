
# O(n) time | O(n) space
def balancedBrackets(string):
    if string is None or len(string) == 0:
        return True

    stack = []
    brackets = {'[': ']', '{': '}', '(': ')'}

    for char in string:
        if char in brackets:
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            open = stack.pop()
            close = brackets[open]
            if char != close:
                return False

    return not stack


def balancedBrackets1(string):
    if string is None or len(string) == 0:
        return True

    map = {'(': ')', '{': '}', '[': ']'}
    closed = set(map.values())
    stack = []

    for c in string:
        if c in map:
            stack.append(map[c])
        elif c in closed:
            if not stack or stack[-1] != c:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    assert balancedBrackets("(a)")
    assert balancedBrackets("([])")
    assert balancedBrackets("([])(){}(())()()")

    assert balancedBrackets1("(a)")
    assert balancedBrackets1("([])")
    assert balancedBrackets1("([])(){}(())()()")
