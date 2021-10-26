# CODE 17: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

from typing import Optional

from SinglyLinkedList import LinkedList, Node


def find_cyclic_node(head: Node) -> Optional[Node]:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break
    
    if not fast: return fast  # Cycle Not Found
    if not fast.next: return fast.next
    fast = head  # Reinitialize fast
    while slow != fast:  # Iterate till cycle starting is found
        slow = slow.next
        fast = fast.next
    return slow


# __main__
def cyclize(head: Node, to_cyclic: int) -> Node:
    if to_cyclic == -1: return head
    # reach Tail
    tail = head
    while tail.next:
        tail = tail.next
    # Find the Node
    ref = head
    while ref and ref.data != to_cyclic:
        ref = ref.next
    
    tail.next = ref
    return head


L = LinkedList()
Head = cyclize(L.construct([87797, 23219, 41441, 58396, 48953, 94603, 2721, 95832, 49029, 98448, 65450]), -1)
X = Head
# for i in range(10):
#     print(X.data, end=" -> ")
#     X = X.next
# print("...")
print(res.data if (res := find_cyclic_node(Head)) else res)
