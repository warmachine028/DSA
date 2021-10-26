# CODE 12: Sort a Binary Linked List

from SinglyLinkedList import Node, LinkedList


def bin_sort(head: Node) -> Node:
    counts_zeros = 0
    ref = head
    while ref:
        counts_zeros += int(not ref.data)
        ref = ref.next
    
    ref = head
    while ref:
        ref.data = int(not counts_zeros > 0)
        counts_zeros -= 1
        ref = ref.next
    return head


L = LinkedList()
print(bin_sort(L.construct([0, 0, 1, 1, 0, 0, 1, 1, 1])))
print(bin_sort(L.construct([])))
print(bin_sort(L.construct([0, 1])))
L.traverse(bin_sort(L.construct([0, 1] * int(10e2))))
print(bin_sort(L.construct([1, 0, 0, 1])))
