# CODE 1: Return the middle node of a linked list
from SinglyLinkedList import Node, LinkedList


def mid(head: Node) -> Node:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


# TESTCASES
L = LinkedList()
print(mid(L.construct([1, 2, 3, 4, 5])).data)  # 3
print(mid(L.construct([1, 2, 4, 5])).data)  # 4
print(mid(L.construct([1, 2, 4, 5, 6, 7])).data)  # 5
print(mid(L.construct([1, 2, 3, 4, 5, 6, 7])).data)  # 4
