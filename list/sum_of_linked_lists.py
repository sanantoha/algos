
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(l1, l2)) time | O(max(l1, l2)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):

    dummy = LinkedList(-1)
    c1 = linkedListOne
    c2 = linkedListTwo
    carry = 0
    c = dummy

    while c1 or c2:
        v1 = c1.value if c1 else 0
        v2 = c2.value if c2 else 0
        sum = v1 + v2 + carry
        carry = sum // 10

        c.next = LinkedList(sum % 10)
        c = c.next

        if c1:
            c1 = c1.next
        if c2:
            c2 = c2.next

    if carry > 0:
        c.next = LinkedList(carry)

    return dummy.next


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


if __name__ == '__main__':
    ll1 = LinkedList(2).addMany([4, 7, 1])
    ll2 = LinkedList(9).addMany([4, 5])
    expected = LinkedList(1).addMany([9, 2, 2])
    actual = sumOfLinkedLists(ll1, ll2)
    print(getNodesInArray(actual))
    assert getNodesInArray(actual) == getNodesInArray(expected)
