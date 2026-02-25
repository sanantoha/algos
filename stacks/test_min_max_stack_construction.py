from stacks.min_max_stack_construction import MinMaxStack, checkMinMaxPeek


def test_min_max_heap():
    stack = MinMaxStack()
    stack.push(5)
    checkMinMaxPeek(5, 5, 5, stack)
    stack.push(7)
    checkMinMaxPeek(5, 7, 7, stack)
    stack.push(2)
    checkMinMaxPeek(2, 7, 2, stack)
    assert stack.pop() == 2
    assert stack.pop() == 7
    checkMinMaxPeek(5, 5, 5, stack)