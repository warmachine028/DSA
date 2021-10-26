# CODE 23: Given a linked list A , reverse the order of all nodes at even positions.
from SinglyLinkedList import Node, LinkedList


def reverse(head: Node) -> Node:
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def reverse_even_nodes(head: Node) -> Node:
    temp = Node()  # To store the head of even nodes LinkedList
    ref = head
    even = temp
    # Splitting the LinkedList into odd and Even nodes
    while ref:
        even.next = ref.next
        even = even.next
        ref.next = even.next if even else None  # Skipping even nodes
        ref = ref.next
    
    # Reversing the Linked List with even nodes
    even = reverse(temp.next)
    ref = head
    # Joining the 2 Linked Lists
    while ref and ref.next or even:
        nex = ref.next if ref else None
        nex2 = even.next
        
        ref.next = even
        even.next = nex
        
        ref = nex
        even = nex2
    return head


L = LinkedList()
print(reverse_even_nodes(L.construct([1, 2, 3, 4, 5, 6, 7, 8, 9])))  # 1 -> 8 -> 3 -> 6 -> 5 -> 4 -> 7 -> 2 -> 9 -> NULL
print(reverse_even_nodes(L.construct([1, 2, 3, 4, 5, 6])))  # 1 -> 6 -> 3 -> 4 -> 5 -> 2 -> NULL
print(reverse_even_nodes(L.construct([1, 2, 3, 4])))  # 1 -> 4 -> 3 -> 2 -> NULL
print(reverse_even_nodes(L.construct([1, 2, 3])))  # 1 -> 2 -> 3 -> NULL
print(reverse_even_nodes(L.construct([1, 2])))  # 1 -> 2 -> NULL
print(reverse_even_nodes(L.construct([1])))  # NULL
print(reverse_even_nodes(L.construct([])))  # NULL
