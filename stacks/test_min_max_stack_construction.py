from stacks.min_max_stack_construction import MinMaxStack, testMinMaxPeek


def test_min_max_heap():
    stack = MinMaxStack()
    stack.push(5)
    testMinMaxPeek(5, 5, 5, stack)
    stack.push(7)
    testMinMaxPeek(5, 7, 7, stack)
    stack.push(2)
    testMinMaxPeek(2, 7, 2, stack)
    assert stack.pop() == 2
    assert stack.pop() == 7
    testMinMaxPeek(5, 5, 5, stack)