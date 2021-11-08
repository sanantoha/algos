
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


if __name__ == '__main__':
    assert balancedBrackets("([])")
    assert balancedBrackets("([])(){}(())()()")