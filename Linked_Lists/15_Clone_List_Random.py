# CODE 15: Copy a linkedList with Random next pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any
# node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
# its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
# should point to new nodes in the copied list such that the pointers in the original list and copied list represent
# the same list state. None of the pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two
# nodes x and y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
# or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

from typing import Optional

from SinglyLinkedList import Node


class NewNode(Node):
    def __init__(self, data, nxt=None, random=None):
        super().__init__(data, nxt)
        self.random: Node = random
    
    def __str__(self):
        return f"Node[{self.data} <{'NULL' if self.random is None else self.random.data}>] -> {self.next or 'NULL'}"


def copy_random_list(head: Optional[NewNode]) -> Optional[NewNode]:
    if not head: return None
    
    # making a copy without random pointer
    ref = head
    while ref:
        ref.next = NewNode(ref.data, ref.next)
        ref = ref.next.next
    # Setting the random pointers
    ref = head
    while ref and ref.next:
        random_node = ref.random
        ref.next.random = random_node.next if random_node else None
        ref = ref.next.next
    
    new_head = head.next
    ref, ref2 = head, new_head
    while ref2:
        ref.next = ref.next.next
        ref2.next = ref2.next.next if ref2.next else None
        ref = ref.next
        ref2 = ref2.next
    
    return new_head


Nodes = NewNode(7), NewNode(13), NewNode(11), NewNode(10), NewNode(1)

Nodes[0].next, Nodes[0].random = Nodes[1], None
Nodes[1].next, Nodes[1].random = Nodes[2], Nodes[0]
Nodes[2].next, Nodes[2].random = Nodes[3], Nodes[4]
Nodes[3].next, Nodes[3].random = Nodes[4], Nodes[2]
Nodes[4].next, Nodes[4].random = None, Nodes[0]

Head = Nodes[0]
print(Head)
print(copy_random_list(Head))
