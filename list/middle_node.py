
from LinkedList import LinkedList


# O(n) time | O(1) space
def middleNode(lst):
    if not lst:
        return lst

    fast = lst
    slow = lst

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


if __name__ == '__main__':
    list = LinkedList(1)
    list.next = LinkedList(2)
    list.next.next = LinkedList(3)
    list.next.next.next = LinkedList(4)

    res = middleNode(list)
    print(res)
    assert res == list.next.next