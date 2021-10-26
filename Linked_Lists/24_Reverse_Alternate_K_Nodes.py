# CODE 24: Problem Description
#
# Given a linked list A of length N and an integer B.
#
# You need to reverse every alternate B nodes in the linked list A.

# INPUT >>  3 -> 4 -> 7 -> 5 -> 6 -> 6 -> 15 -> 61 -> 16 -> NULL, 3
# OUTPUT >> 7 -> 4 -> 3 -> 5 -> 6 -> 6 -> 16 -> 61 -> 15 -> NULL

# INPUT >>  1 -> 4 -> 6 -> 6 -> 4 -> 10 -> NULL, 2
# OUTPUT >> 4 -> 1 -> 6 -> 6 -> 10 -> 4 -> NULL

from SinglyLinkedList import Node, LinkedList


def size(head: Node) -> int:
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def reverse_alternate_groups(head: Node, k: int) -> Node:
    if not k or not head or not head.next: return head
    ref = head
    prev = None
    # Reversing the k nodes at first
    for _ in range(k):
        if not ref: return prev
        nex = ref.next
        ref.next = prev
        prev = ref
        ref = nex
    
    # Skipping the k nodes at last
    head.next = ref
    for _ in range(k - 1):
        if not ref: return prev
        ref = ref.next
    
    ref.next = reverse_alternate_groups(ref.next, k)
    return prev


L = LinkedList()
print(reverse_alternate_groups(L.construct([1, 2, 3, 4, 5, 6]), 3))  # 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> NULL
print(reverse_alternate_groups(L.construct([1, 2, 3, 4, 5, 6]), 2))  # 2 -> 1 -> 3 -> 4 -> 6 -> 5 -> NULL
print(reverse_alternate_groups(L.construct([1, 2, 3, 4, 5, 6]), 4))  # 4 -> 3 -> 2 -> 1 -> 5 -> 6 -> NULL
print(reverse_alternate_groups(L.construct([1, 2, 3, 4, 5, 6]), 5))  # 5 -> 4 -> 3 -> 2 -> 1 -> 6 -> NULL
print(reverse_alternate_groups(L.construct([1, 2]), 4))  # 2 -> 1 -> NULL
