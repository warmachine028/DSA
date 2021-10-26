# CODE 26: Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes
# of the list from position left to position right, and return the reversed list.
#
# 1 -> 2 -> 3 -> 4 -> 5 -> NULL, left = 2, right = 4
# 1 -> 4 -> 3 -> 2 -> 5 -> NULL
#
from typing import Optional

from SinglyLinkedList import Node, LinkedList


def reverse_till_k(node: Node, k: int) -> Node:
    if not node: return node
    first = node
    prev = None
    for _ in range(k + 1):
        nex = node.next
        node.next = prev
        prev = node
        node = nex
    first.next = node
    return prev


def reverse_2(head: Optional[Node], left: int, right: int) -> Optional[Node]:
    temp = Node(0)
    
    prev = temp  # To traverse the temporary Node
    ref = head  # To traverse the LinkedList
    for _ in range(1, left):  # To skip left nodes (left - 1) for 0 based indexing
        prev.next = ref
        ref = ref.next
        prev = prev.next
    
    # Reversing till right Nodes
    prev.next = reverse_till_k(ref, right - left)
    return temp.next


L = LinkedList()
print(reverse_2(L.construct([1, 2, 3, 4, 5]), 2, 4))  # 1 -> 4 -> 3 -> 2 -> 5 -> NULL
print(reverse_2(L.construct([1, 2, 3, 4, 5]), 1, 5))  # 5 -> 4 -> 3 -> 2 -> 1 -> NULL
print(reverse_2(L.construct([1, 2, 3, 4, 5]), 2, 5))  # 1 -> 5 -> 4 -> 3 -> 2 -> NULL
print(reverse_2(L.construct([1, 2, 3, 4, 5]), 2, 5))  # 1 -> 5 -> 4 -> 3 -> 2 -> NULL
print(reverse_2(L.construct([1, 2, 3, 4, 5]), 1, 1))  # 1 -> 2 -> 3 -> 4 -> 5 -> NULL
print(reverse_2(L.construct([1, 2, 3, 4, 5]), 5, 5))  # 1 -> 2 -> 3 -> 4 -> 5 -> NULL
print(reverse_2(L.construct([1, 2, 3, 4]), 2, 3))  # 1 -> 3 -> 2 -> 4 -> NULL
print(reverse_2(L.construct([1, 2]), 1, 2))  # 2 -> 1 -> NULL
print(reverse_2(L.construct([1]), 1, 1))  # 1 -> NULL
print(reverse_2(L.construct([*range(1, 26)]), 3, 9))  #
