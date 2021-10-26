# CODE 11b: Given a doubly linked list containing n nodes, where each node is at most k away from its target position
# in the list. The problem is to sort the given doubly linked list. For example, let us consider k is 2,
# a node at position 7 in the sorted doubly linked list, can be at positions 5, 6, 7, 8, 9 in the given doubly linked
# list.
# Examples:
# List: 3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8 -> NULL, K: 2
# Sorted: 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56 -> NULL
from heapq import heappush, heappop

from Linked_Lists.DoublyLinkedList import DoublyLinkedList, Node


# Sorting using min Heap
def sort_k_sorted(head: Node, k: int) -> Node:  # Time Complexity: O(n*k) Space Complexity: O(1)
    if not head: return head
    priority_queue = []
    temp = Node()
    
    for i in range(k + 1):
        if not head:
            break
        heappush(priority_queue, (head.data, head))
        head = head.next
    
    ref = temp
    while priority_queue:  # Loop until Priority queue is empty
        node = heappop(priority_queue)[1]
        node.prev = ref
        ref.next = node
        ref = ref.next
        if head:  # Insert items in Priority queue until all items are fully inserted
            heappush(priority_queue, (head.data, head))
            head = head.next
    
    temp.next.prev = ref.next = None
    return temp.next


def test(items: list[int], k: int) -> None:
    D.__init__(items)
    # head = sort_k_sorted(D.head, k)
    head = sort_k_sorted(D.head, k)
    print(head)  # Printing in Forward
    while head and head.next: head = head.next
    print(head.__str__(reverse=True) if head else None)  # Printing in reverse


D = DoublyLinkedList()
test([3, 6, 2, 12, 56, 8], 2)
# 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56 -> NULL
# 56 <-> 12 <-> 8 <-> 6 <-> 3 <-> 2 -> NULL

# test([1, 3, 2, 5, 4], 2)
# 1 <-> 2 <-> 3 <-> 4 <-> 5 -> NULL
# 5 <-> 4 <-> 3 <-> 2 <-> 1 -> NULL

test([1], 1)
# 1 <-> NULL
# 1 <-> NULL

test([], 0)
# NULL
# NULL
