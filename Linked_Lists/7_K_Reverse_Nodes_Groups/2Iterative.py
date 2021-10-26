# CODE 7b: Given a singly linked list and an integer K, reverses the nodes of the list K at a time and returns modified
# linked list.

# Example :
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
#
# Try to solve the problem using constant extra space.
from Linked_Lists.SinglyLinkedList import Node, LinkedList


# Iterative Approach
def reverse_k_nodes(head: Node, k: int) -> Node:
    first = Node(0)
    tail = first
    ref = head
    while ref:
        node = ref
        count = k
        while node and count:  # checking if k - 1 Nodes exist
            node = node.next
            count -= 1
        if count:  # k- 1 nodes doesnt exist
            tail.next = ref  # Assigning rest of the nodes to tail
            break
        
        future_tail = ref  # Storing the future tail
        prev = None
        for _ in range(k):  # Reversing the Nodes
            nex = ref.next
            ref.next = prev
            prev = ref
            ref = nex
        tail.next = prev  # Linking past Tail to new head
        tail = future_tail  # Assigning tail to future tail
    return first.next


# __main__
L = LinkedList()
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5, 6]), 2))  # 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5, 6]), 3))  # 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4, 5]), 3))  # 3 -> 2 -> 1 -> 4 -> 5 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3, 4]), 1))  # 1 -> 2 -> 3 -> 4 -> NULL
print(reverse_k_nodes(L.construct([1]), 1))  # 1 -> NULL
print(reverse_k_nodes(L.construct([1, 2, 3]), 2))  # 2 -> 1 -> NULL
