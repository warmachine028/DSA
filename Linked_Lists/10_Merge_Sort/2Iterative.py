# CODE 10b: Perform merge sort in a Linked List using Iterative Approach

import random
from typing import Optional

from Linked_Lists.SinglyLinkedList import LinkedList, Node


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    current = head
    if not current or not current.next:
        return current
    
    middle = find_middle(current)
    next_middle = middle.next
    middle.next = None
    left = merge_sort(current)
    right = merge_sort(next_middle)
    return merge(left, right)


def find_middle(head: Node) -> Node:
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


# Iterative Approach
def merge(first: Node, second: Node) -> Node:
    if not first:
        return second
    if not second:
        return first
    
    if first.data > second.data:
        result = second
        second = second.next
    else:
        result = first
        first = first.next
    
    ref = result
    while first and second:
        if first.data > second.data:
            result.next = second
            second = second.next
        else:
            result.next = first
            first = first.next
        result = result.next
    result.next = first if not second else second
    return ref


L = LinkedList()
L.traverse(merge_sort(L.construct([1, 4, 3, 2, 1, 3])))
L.traverse(merge_sort(L.construct([1, 2, 3, 4, 1, 2])))
L.traverse(merge_sort(L.construct([2, 1])))
L.traverse(merge_sort(L.construct([random.randrange(1, 1000) for i in range(1, int(10e4))])))
