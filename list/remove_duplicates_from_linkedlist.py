from list.LinkedList import LinkedList


def remove_duplicates_from_linked_list(linked_list):
    curr = linked_list

    while curr is not None:
        next_node = curr.next
        while next_node is not None and curr.value == next_node.value:
            next_node = next_node.next

        curr.next = next_node
        curr = curr.next

    return linked_list


if __name__ == '__main__':
    test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
    print(remove_duplicates_from_linked_list(test))
