from typing import Optional

from SinglyLinkedList import LinkedList, Node


def partition(head: Optional[Node], x: int) -> Optional[Node]:
    low = lower = Node()
    high = higher = Node()
    
    while head:
        if head.data < x:
            low.next = head
            low = low.next
        else:
            high.next = head
            high = high.next
        head = head.next
    
    high.next = None
    low.next = higher.next
    return lower.next


L = LinkedList()
print(partition(L.construct([1, 4, 3, 2, 5, 2]), 3))  # 1 -> 2 -> 2 -> NULL + 4 -> 3 -> 5 -> NULL
print(partition(L.construct([2, 1]), 2))  # 1 -> NULL + 2 -> NULL
print(partition(L.construct([*range(10, 0, -1)]), 5))  # 4 -> 3 -> 2 -> 1 -> NULL + 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> NULL
