# CODE 4b: Given a sorted linked list, delete all duplicates such that each element appear only once.
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

from Linked_Lists.SinglyLinkedList import Node, LinkedList


# Iterative Approach
def remove_duplicate_sorted(head: Node) -> Node:
    ref = head
    while ref.next:
        if ref.data == ref.next.data:
            ref.next = ref.next.next
        else:
            ref = ref.next
    return head


# TESTCASES
L = LinkedList()
print(remove_duplicate_sorted(L.construct([1, 1, 2])))  # 1->2->NULL
print(remove_duplicate_sorted(L.construct([1, 1, 2, 3, 3])))  # 1->2->3->NULL
print(remove_duplicate_sorted(L.construct([1])))  # 1->NULL
