# CODE 25:
# Reorder List:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
# 1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5 -> NULL
#
# L0 -> L1 -> L2 -> L3 -> ...-> Ln-3 -> Ln-2 -> Ln-1 -> Ln -> NULL
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> L3 -> Ln-3 -> ...-> NULL
from SinglyLinkedList import Node, LinkedList


def mid_finder(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse(node: Node) -> Node:
    prev = None
    while node:
        nex = node.next
        node.next = prev
        prev = node
        node = nex
    return prev


def reorder(head: Node) -> Node:
    if not head or not head.next: return head
    mid = mid_finder(head)
    tail = reverse(mid)
    mid.next = None
    
    ref = head
    while ref.next and tail.next:
        nex = ref.next
        nex2 = tail.next
        
        ref.next = tail
        tail.next = nex
        
        ref = nex
        tail = nex2
    return head


L = LinkedList()
print(reorder(L.construct([1, 2, 3, 4, 5, 6, 7, 8])))  # 1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5 -> NULL
print(reorder(L.construct([1, 2, 3, 4, 5])))  # 1 -> 4 -> 2 -> 4 -> 3 -> 6 -> 4 -> 5 -> NULL
print(reorder(L.construct([1, 2, 3, 4])))  # 1 -> 4 -> 2 -> 3 -> NULL
print(reorder(L.construct([1, 2, 3])))  # 1 -> 3 -> 2 -> NULL
print(reorder(L.construct([1, 2])))  # 1 -> 2 -> NULL
