# CODE 7c: Given a singly linked list and an integer K, reverses the nodes of the list K at a time and returns modified
# linked list.

# Example :
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
#
# Try to solve the problem using constant extra space.
from Linked_Lists.SinglyLinkedList import Node, LinkedList


def size(head: Node) -> int:
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def reverse_k_nodes(head: Node, k: int) -> Node:
    temp = Node(0)
    ref, ref1 = head, temp
    length_ = size(head)
    i = 0
    while i < length_ - length_ % k:
        prev = None
        last = ref
        for j in range(k):
            nex = ref.next
            ref1.next = last
            ref.next = prev
            prev = ref
            ref = nex
        ref1.next = prev
        ref1 = last
        i += k
    ref1.next = ref
    
    return temp.next


# __main__
L = LinkedList()
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5, 6]), 2))  # 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5, 6]), 3))  # 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5]), 3))  # 3 -> 2 -> 1 -> 4 -> 5 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4]), 1))  # 1 -> 2 -> 3 -> 4 -> NULL
print(reverse_k_nodes(L.construct([1]), 1))  # 1 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3]), 2))  # 2 -> 1 -> NULL
