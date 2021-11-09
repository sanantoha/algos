
# O(n ^ 2) | O(n) space
def sortStack(stack):
    if stack is None or len(stack) == 0:
        return stack

    top = stack.pop()
    return insert(sortStack(stack), top)



def insert(stack, elem):
    if not stack:
        stack.append(elem)
        return stack
    else:
        top = stack.pop()
        if elem <= top:
            stack = insert(stack, elem)
            stack.append(top)
        else:
            stack = insert(stack, top)
            stack.append(elem)
        return stack


if __name__ == '__main__':
    input = [-5, 2, -2, 4, 3, 1]
    expected = [-5, -2, 1, 2, 3, 4]
    actual = sortStack(input)
    print(actual)
    assert actual == expected
