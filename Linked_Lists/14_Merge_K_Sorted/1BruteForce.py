# CODE 14a: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# # Merge all the linked-lists into one sorted linked-list and return it.

# Brute Force Approach:
# Time Complexity: (Tim Sort Time Complexity): O(N * log(N))
# Space Complexity: O(k * n)

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def merge_k_sorted(heads: list[Node]) -> Node:
    nodes = []
    for head in heads:
        while head:
            nodes.append(head)
            head = head.next
    new_head = Node(0)
    ref = new_head
    for node in sorted(nodes, key=lambda n: n.data):
        ref.next = node
        ref = ref.next
    return new_head.next


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
