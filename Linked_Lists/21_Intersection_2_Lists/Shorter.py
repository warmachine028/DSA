# CODE 21a: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists
# intersect.
# If the two linked lists have no intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:

#       a1 -> a2 \
#                 c1 -> c2 -> c3 -> NULL
# b1 -> b2 -> b3 /

from typing import Optional

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def detect_intersection(head1: Node, head2: Node) -> Optional[Node]:
    a_ = head1
    b_ = head2
    while a_ != b_:
        a_ = a_.next if a_ else head2
        b_ = b_.next if b_ else head1
    return a_


# __main__
def join(head1: Node, head2: Node, head3: Node) -> None:
    temp = [head1, head2]
    while temp[0] and temp[0].next: temp[0] = temp[0].next
    while temp[1] and temp[1].next: temp[1] = temp[1].next
    if temp[0] or temp[1]: temp[0].next = temp[1].next = head3


L = LinkedList()
a, b, c = L.construct([1, 9, 1]), L.construct([3]), L.construct([2, 4])
join(a, b, c)
print(res.data if (res := detect_intersection(a, b)) else None)  # 2

a, b, c = L.construct([2, 6, 4]), L.construct([1, 5]), L.construct([])
join(a, b, c)
print(res.data if (res := detect_intersection(a, b)) else None)  # NULL

a, b, c = L.construct([3]), L.construct([1, 9, 1]), L.construct([2, 4])
join(a, b, c)
print(res.data if (res := detect_intersection(a, b)) else None)  # 2

a, b, c = L.construct([4, 5, 6]), L.construct([1, 2, 3]), L.construct([])
join(a, b, c)
print(res.data if (res := detect_intersection(a, b)) else None)  # NULL
