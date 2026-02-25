
# Feel free to add new properties and methods to the class.
class MinMaxStack:

    class Node:
        def __init__(self, val, min, max):
            self.val = val
            self.min = min
            self.max = max

    def __init__(self):
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[len(self.stack) - 1].val

    # O(1) time | O(1) space
    def pop(self):
        if len(self.stack) == 0:
            return -1
        node = self.stack.pop()
        return node.val

    # O(1) time | O(1) space
    def push(self, number):
        if len(self.stack) == 0:
            self.stack.append(self.Node(number, number, number))
        else:
            node = self.stack[len(self.stack) - 1]
            self.stack.append(self.Node(number, min(node.min, number), max(node.max, number)))

    # O(1) time | O(1) space
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[len(self.stack) - 1].min

    # O(1) time | O(1) space
    def getMax(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[len(self.stack) - 1].max


def checkMinMaxPeek(min_val, max_val, peek, stack):
    assert stack.getMin() == min_val
    assert stack.getMax() == max_val
    assert stack.peek() == peek


if __name__ == '__main__':
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