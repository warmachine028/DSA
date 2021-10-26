# CODE 9b: Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be
# changed.

from Linked_Lists.SinglyLinkedList import Node, LinkedList


# Recursive Approach
def swap_pair(head: Node) -> Node:
    if not head or not head.next: return head
    node1 = head.next
    node2 = node1.next
    node1.next = head
    head.next = swap_pair(node2)
    return node1


L = LinkedList()
print(swap_pair(L.construct([1, 2, 3, 4])))  # 2 -> 1 -> 4 -> 3 -> NULL
print(swap_pair(L.construct([1, 2, 3, 4, 5])))  # 2 -> 1 -> 4 -> 3 -> NULL
print(swap_pair(L.construct([1])))  # 1 -> NULL
print(swap_pair(L.construct([])))  # NONE
