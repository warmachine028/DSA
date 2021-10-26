# CODE 18a: Insertion Sort a Singly linked List

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def insertion_sort(head: Node) -> Node:  # Time Complexity: O(N^2),  Space Complexity: O(1)
    if not head: return head
    temp = Node(0, head)
    ref = head
    while ref.next:
        key = ref.next.data
        if ref.data < key:
            ref = ref.next
            continue
        
        prev = temp
        while prev.next.data < key:
            prev = prev.next
        
        t = ref.next
        ref.next = t.next
        t.next = prev.next
        prev.next = t
    return temp.next


L = LinkedList()
print(insertion_sort(L.construct([2, 1, 3, 1, 5, 7])))  # 1 -> 1 -> 2 -> 3 -> 5 -> 7 -> NULL
print(insertion_sort(L.construct([1, 2, 3])))  # 1 -> 2 -> 3 -> NULL
print(insertion_sort(L.construct([1])))  # 1 -> NULL
print(insertion_sort(L.construct([])))  # NULL
print(insertion_sort(L.construct([1, 2, -1])))  # -1-> 1 -> 2 -> NULL
print(insertion_sort(L.construct([-1, 5, 9, 8, 0])))  # -1-> 1 -> 2 -> NULL
