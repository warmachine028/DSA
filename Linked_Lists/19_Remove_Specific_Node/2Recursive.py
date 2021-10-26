# CODE 19b: Given the head of a linked list and an integer val, remove all the nodes of the linked list
# that has Node.val == val, and return the new head.

from typing import Optional

from Linked_Lists.SinglyLinkedList import Node, LinkedList


# Using Recursion
def remove_node(head: Optional[Node], data: int) -> Optional[Node]:
    if not head: return head
    head.next = remove_node(head.next, data)
    return head.next if head.data == data else head


L = LinkedList()
print(remove_node(L.construct([1, 2, 2, 2, 2, 2, 1, 1]), 2))  # 1 -> 1 -> 1 -> NULL
print(remove_node(L.construct([]), 2))  # 2 -> NULL
print(remove_node(L.construct([2, 1, 2]), 2))  # 1 -> NULL
print(remove_node(L.construct([2]), 2))  # NULL
print(remove_node(L.construct([2, 2, 2, 2]), 2))  # NULL
print(remove_node(L.construct([1, 2, 0, 2]), 2))  # 1 -> 0 -> NULL
print(remove_node(L.construct([1, 3, 4, 6, 11, 56] + [2] * int(10e4 - 7)), 2))  # 1 -> 3 -> 4 -> 6 -> 11 -> 56 -> NULL
print(remove_node(L.construct([1, 2] * int(10e4 // 2)), 2))  # 1 -> 3 -> 4 -> 6 -> 11 -> 56 -> NULL
print(remove_node(L.construct([1, 2, 3, 4] * int(10e4 // 4)), 2))  # 1 -> 3 -> 4 -> 6 -> 11 -> 56 -> NULL
