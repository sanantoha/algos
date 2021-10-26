
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth_node_from_end(head, k):
    if head is None:
        return

    curr = head
    n = k
    while n > 0 and curr is not None:
        curr = curr.next
        n -= 1

    if n > 0:
        return

    if curr is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    fast = curr
    slow = head

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    next_node = slow.next
    if next_node is not None:
        slow.next = next_node.next


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList
# if hasattr(program, "LinkedList"):
#     linkedListClass = program.LinkedList

class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


if __name__ == '__main__':
    test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
    expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
    remove_kth_node_from_end(test, 4)
    print(test.getNodesInArray())
    assert test.getNodesInArray() == expected.getNodesInArray()