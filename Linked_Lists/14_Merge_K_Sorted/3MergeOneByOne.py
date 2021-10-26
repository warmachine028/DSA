# CODE 14b: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Merge One by One:
# Time Complexity: O(K * n)
# Space Complexity: O(1)

from functools import reduce

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def merge(head1: Node, head2: Node) -> Node:
    if head1 is None: return head2
    if head2 is None: return head1
    
    if head1.data > head2.data:
        head = head2
        head2 = head2.next
    else:
        head = head1
        head1 = head1.next
    
    ref = head
    while head1 and head2:
        if head1.data > head2.data:
            ref.next = head2
            head2 = head2.next
        else:
            ref.next = head1
            head1 = head1.next
        ref = ref.next
    
    ref.next = head2 or head1
    return head


def merge_k_sorted(heads: list[Node]) -> Node:
    return reduce(lambda head1, head2: merge(head1, head2), heads) if heads else heads


L = LinkedList()

temp = [
    L.construct([1, 2, 3, 4]),
    L.construct([1, 2, 3]),
    L.construct([1, 3]),
    L.construct([5, 6, 8]),
]
L.traverse(merge_k_sorted(temp))
temp = [L.construct([])]
L.traverse(merge_k_sorted(temp))
