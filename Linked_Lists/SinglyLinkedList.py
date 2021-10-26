# Helper Functions and Classes for linkedList programs
import sys

from typing import Optional

sys.setrecursionlimit(int(10e4))


class Node:
    def __init__(self, data: Optional[int] = 0, nex=None) -> None:
        self.data = data
        self.next = nex
    
    def __str__(self):
        return f"Node{[self.data]} -> {self.next or 'NULL'}"


class LinkedList:
    def construct(self, items: list[int]) -> Optional[Node]:
        if not items:
            return None
        head = Node(items.pop(0))
        ref = head
        while items:
            ref.next = Node(items.pop(0))
            ref = ref.next
        return head
    
    @staticmethod
    def traverse(head):
        if head is None:
            print('NULL')
            return
        ref = head
        while ref.next:
            print(ref.data, end=' -> ')
            ref = ref.next
        print(ref.data, '-> NULL')


if __name__ == '__main__':
    # TEST
    L = LinkedList()
    H = L.construct([1, 2, 3, 4, 5, 6, 7, 8])
    L.traverse(H)
    y = Node(90)
    x = Node(10, y)
    print(x)
    H = L.construct([1, 2] * int(10e3))
    print(H)
