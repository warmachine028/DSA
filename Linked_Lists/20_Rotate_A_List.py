# CODE 20: Given the head of a linked list, rotate the list to the right by k places.

from SinglyLinkedList import LinkedList, Node


def rotate(head: Node, k) -> Node:
    if not head or not head.next: return head
    
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    tail.next = head
    k = k % length
    k = length - k
    
    for i in range(k - 1):
        head = head.next
    
    temp = head.next
    head.next = None
    return temp


L = LinkedList()
print(rotate(L.construct([1, 2, 3, 4, 5]), 2))  # 4, 5, 1, 2, 3
print(rotate(L.construct([0, 1, 2]), 4))  # 2, 0, 1
print(rotate(L.construct([0]), 4))  # 0
print(rotate(L.construct([1, 2]), 4))  # 1, 2
print(rotate(L.construct([1, 2]), 0))  # 1, 2
print(rotate(L.construct([1]), 0))  # 1
print(rotate(L.construct([1, 2, 3]), 3))  # 1, 2, 3
print(rotate(L.construct([91, 34, 18, 83, 38, 82, 21, 69]), 89))  # 69 , 91, 34, 18, 83, 38, 82, 21, 69
