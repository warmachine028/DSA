# CODE 14d: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# # Merge all the linked-lists into one sorted linked-list and return it.

# Using Divide and Conquer:
# Time Complexity: O(Nlog(k))
# Space Complexity: O(1)

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def merge_k_sorted(heads: list[Node]) -> Node:
    length = len(heads)
    gap = 1
    while gap < length:
        for i in range(0, length - gap, gap * 2):
            heads[i] = merge_2_sorted(heads[i], heads[gap + i])
        gap *= 2
    
    return heads[0] if heads else None


def merge_2_sorted(head1: Node, head2: Node) -> Node:
    if not head1: return head2
    if not head2: return head1
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
temp = []
L.traverse(merge_k_sorted(temp))
