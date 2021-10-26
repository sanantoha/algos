
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return

        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    # O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return

        curr_pos = 1
        curr = self.head
        while position != curr_pos and curr is not None:
            curr = curr.next
            curr_pos += 1

        if curr is not None:
            self.insertBefore(curr, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        curr = self.head
        while curr is not None:
            nodeToRemove = curr
            curr = curr.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        self.removeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head

        while node:
            if node.value == value:
                return True
            node = node.next

        return False

    def removeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.next = None
        node.prev = None


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


if __name__ == '__main__':
    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    # three2 = Node(3)
    # three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    linkedList.setHead(one)
    linkedList.insertAfter(one, two)
    linkedList.insertAfter(two, three)
    linkedList.insertAfter(three, four)
    linkedList.insertAfter(four, five)
    linkedList.insertAfter(five, six)
    seven = Node(7)
    linkedList.insertAfter(six, seven)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(7, one)
    print(getNodeValuesHeadToTail(linkedList))
    linkedList.insertAtPosition(1, one)
    print(getNodeValuesHeadToTail(linkedList))
    linkedList.insertAtPosition(2, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(3, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(4, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(5, one)
    print(getNodeValuesHeadToTail(linkedList))

    linkedList.insertAtPosition(6, one)
    print(getNodeValuesHeadToTail(linkedList))
    # bindNodes(one, two)
    # bindNodes(two, three)
    # bindNodes(three, four)
    # bindNodes(four, five)
    # linkedList.head = one
    # linkedList.tail = five
    #
    # linkedList.setHead(four)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5]
    # assert getNodeValuesTailToHead(linkedList) == [5, 3, 2, 1, 4]
    #
    # linkedList.setTail(six)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5, 6]
    # assert getNodeValuesTailToHead(linkedList) == [6, 5, 3, 2, 1, 4]
    #
    # linkedList.insertBefore(six, three)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6]
    # assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 1, 4]
    #
    # linkedList.insertAfter(six, three2)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6, 3]
    # assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4]
    #
    # linkedList.insertAtPosition(1, three3)
    # assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
    # assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4, 3]
    #
    # linkedList.removeNodesWithValue(3)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 6]
    # assert getNodeValuesTailToHead(linkedList) == [6, 5, 2, 1, 4]
    #
    # linkedList.remove(two)
    # assert getNodeValuesHeadToTail(linkedList) == [4, 1, 5, 6]
    # assert getNodeValuesTailToHead(linkedList) == [6, 5, 1, 4]
    #
    # assert linkedList.containsNodeWithValue(5)