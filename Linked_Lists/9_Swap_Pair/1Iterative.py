# CODE 9a: Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be
# changed.

from Linked_Lists.SinglyLinkedList import Node, LinkedList


# Iterative Approach
def swap_pair(head: Node) -> Node:
    temp = Node(0, head)
    ref = temp
    while (node1 := ref.next) and (node2 := node1.next):
        node1.next = node2.next
        node2.next = node1
        ref.next = node2
        ref = node2.next
    return temp.next


L = LinkedList()
print(swap_pair(L.construct([1, 2, 3, 4])))  # 2 -> 1 -> 4 -> 3 -> NULL
print(swap_pair(L.construct([1, 2, 3, 4, 5])))  # 2 -> 1 -> 4 -> 3 -> NULL
print(swap_pair(L.construct([1])))  # 1 -> NULL
print(swap_pair(L.construct([])))  # NONE
