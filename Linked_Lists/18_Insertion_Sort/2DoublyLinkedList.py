# CODE 18b: Insertion Sort a doubly linked List

import random
from typing import Optional

from Linked_Lists.DoublyLinkedList import DoublyLinkedList, Node


def sort(head: Node) -> Node:
    sorted_ = None  # Init a doubly sorted Linked List
    ref = head
    while ref:
        next_ = ref.next  # Store next for next iteration
        ref.prev = ref.next = None
        sorted_ = insert(sorted_, ref)
        ref = next_
    
    return sorted_


def insert(head: Optional[Node], node: Node) -> Node:
    if not head:  # Linked List Empty
        head = node
    elif head.data >= node.data:  # Node to insert at the beginning of the list
        node.next = head
        node.next.prev = node
        head = node
    else:
        ref = head
        # Locating the node after which the node is to be inserted
        while ref.next and ref.next.data < node.data:
            ref = ref.next
        node.next = ref.next
        if ref.next: ref.next.prev = node
        ref.next = node
        node.prev = ref
    return head


D = DoublyLinkedList((lambda x: (random.shuffle(x), x)[1])([*range(10)]))
print(D)
print(D.__str__(True))
print(sort(D.head))
