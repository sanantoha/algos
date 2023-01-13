
from LinkedList import LinkedList


# O(l1 + l2) time | O(1) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    l1 = linkedListOne
    l2 = linkedListTwo

    while l1 != l2:
        l1 = l1.next if l1 else linkedListTwo
        l2 = l2.next if l2 else linkedListOne

    return l1


if __name__ == '__main__':
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(3)
    l1.next.next.next = LinkedList(4)

    l2 = LinkedList(10)
    l2.next = LinkedList(20)
    l2.next.next = l1.next.next

    actual = mergingLinkedLists(l1, l2)
    print(actual)
    assert actual.getNodesInArray() == [3, 4]