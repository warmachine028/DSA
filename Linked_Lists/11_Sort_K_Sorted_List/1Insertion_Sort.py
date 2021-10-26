# CODE 11a: Given a doubly linked list containing n nodes, where each node is at most k away from its target position
# in the list. The problem is to sort the given doubly linked list. For example, let us consider k is 2,
# a node at position 7 in the sorted doubly linked list, can be at positions 5, 6, 7, 8, 9 in the given doubly linked
# list.
# Examples:
# List: 3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8 -> NULL, K: 2
# Sorted: 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56 -> NULL
from Linked_Lists.DoublyLinkedList import DoublyLinkedList, Node


# Sorting using insertion sort
def sort_k_sorted(head: Node, k: int) -> Node:
    if not head: return head
    temp = Node(0, head)
    ref = head
    while ref.next:
        key = ref.next.data
        if ref.data > key:
            prev = temp
            # Reach the position to insert
            while prev.next.data < key:
                prev = prev.next
            
            # Perform Insertion Operation
            temp_ = prev.next
            
            prev.next = ref.next
            ref.next.prev = prev
            
            ref.next = prev.next.next
            if ref.next: ref.next.prev = ref
            
            prev.next.next = temp_
            temp_.prev = prev.next
            continue
        
        ref = ref.next
    temp.next.prev = None
    return temp.next


def test(items: list[int], k: int) -> None:  # Time Complexity O(n*k) Space Complexity: O(1)
    D.__init__(items)
    head = sort_k_sorted(D.head, k)
    print(head)  # Printing in Forward
    while head and head.next: head = head.next
    print(head.__str__(reverse=True) if head else None)  # Printing in reverse


D = DoublyLinkedList()
test([3, 6, 2, 12, 56, 8], 2)
# 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56 -> NULL
# 56 <-> 12 <-> 8 <-> 6 <-> 3 <-> 2 -> NULL

test([1, 3, 2, 5, 4], 2)
# 1 <-> 2 <-> 3 <-> 4 <-> 5 -> NULL
# 5 <-> 4 <-> 3 <-> 2 <-> 1 -> NULL

test([1], 1)
# 1 <-> NULL
# 1 <-> NULL

test([], 0)
# NULL
# NULL
