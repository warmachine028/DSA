# CODE 15: Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
#
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.

from SinglyLinkedList import Node, LinkedList


def reverse_m_to_n(head: Node, m: int, n: int) -> Node:
    temp = Node(0)
    temp.next = head
    ref = temp
    for _ in range(m - 1): ref = ref.next
    
    first, last = ref, ref.next
    ref = last
    prev = None
    
    for _ in range(n - m + 1):
        next_ = ref.next
        ref.next, prev, ref = prev, ref, next_
    
    first.next = prev
    last.next = ref
    return temp.next


L = LinkedList()
print(reverse_m_to_n(L.construct([1, 2, 3, 4, 5]), 2, 4))  # 1->4->3->2->5->NULL
print(reverse_m_to_n(L.construct([1, 2, 3]), 1, 3))  # 3->2->1->NULL
print(reverse_m_to_n(L.construct([1, 2, 3]), 1, 2))  # 2->1->3->NULL
print(reverse_m_to_n(L.construct([1]), 1, 1))  # 1->NULL
print(reverse_m_to_n(L.construct([1, 2, 3, 4, 5]), 4, 5))  # 1->2->3->5->4->NULL
print(reverse_m_to_n(L.construct([1, 2, 3, 4, 5]), 1, 1))  # 1->2->3->5->4->NULL
print(reverse_m_to_n(L.construct([1, 2, 3, 4, 5]), 3, 4))  # 1->2->4->3->5->NULL
print(reverse_m_to_n(L.construct([1, 2, 3, 4, 5]), 1, 5))  # 5->4->3->2->1->NULL
