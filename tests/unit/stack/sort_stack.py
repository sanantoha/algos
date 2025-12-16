from stacks.sort_stack import sortStack, sortStack1

input = [-5, 2, -2, 4, 3, 1]
expected = [-5, -2, 1, 2, 3, 4]


def test_sort_stack():
    actual = sortStack(input)
    print(actual)
    assert actual == expected


def test_sort_stack1():
    actual = sortStack1(input)
    print(actual)
    assert actual == expected