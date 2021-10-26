# CODE 14d: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Divide and Conquer Approach using Min Heap:
# Time Complexity: O(n*log(k))
# Space Complexity: O(k)

from heapq import heappop, heapify, heappush

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def merge_k_sorted(heads: list[Node]) -> Node:
    head = Node(0)
    h = [(h.data, i) for i, h in enumerate(heads) if h]
    heapify(h)
    ref = head
    while h:
        data, index = heappop(h)
        ref.next = Node(data)
        ref = ref.next
        node = heads[index] = heads[index].next
        if node: heappush(h, (node.data, index))
    
    return head.next


L = LinkedList()

temp = [
    L.construct([1, 2, 3, 4]),
    L.construct([1, 2, 3]),
    L.construct([1, 3]),
    L.construct([5, 6, 8])
]
L.traverse(merge_k_sorted(temp))  # 1 -> 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4 -> 5 -> 6 -> 8 -> NULL

temp = [L.construct([])]
L.traverse(merge_k_sorted(temp))  # NULL

temp = []
L.traverse(merge_k_sorted(temp))  # NULL
