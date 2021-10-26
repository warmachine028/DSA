# CODE 7a: Given a singly linked list and an integer K, reverses the nodes of the list K at a time and returns modified
# linked list.
#
#
# Example :
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
#
# Try to solve the problem using constant extra space.

from typing import Optional

from Linked_Lists.SinglyLinkedList import Node, LinkedList


# Recursive Approach
def reverse_k_nodes(head: Node, k: int) -> Optional[Node]:
    ref = head
    count = k
    while ref and count:
        ref = ref.next
        count -= 1
    if count: return head
    
    prev = nex = None
    ref = head
    for _ in range(k):
        nex = ref.next
        ref.next = prev
        prev = ref
        ref = nex
    
    head.next = reverse_k_nodes(nex, k)
    return prev


# __main__
# TEST CASES
L = LinkedList()
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5, 6]), 2))  # 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5, 6]), 3))  # 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5]), 3))  # 3 -> 2 -> 1 -> 4 -> 5 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4]), 1))  # 1 -> 2 -> 3 -> 4 -> NULL
print(reverse_k_nodes(L.construct([1]), 1))  # 1 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3]), 2))  # 2 -> 1 -> 3 -> NULL
