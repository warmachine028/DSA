# CODE 3: Given a linked list A of length N and an integer B.
#
# You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.
#
# If no such element exists, then return -1.
#
# NOTE:
#
# Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.

from SinglyLinkedList import Node, LinkedList


def middle_node(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def kth_node_mid(head: Node, k) -> int:
    stack = []
    mid = middle_node(head)
    ref = head
    while ref != mid:
        stack.append(ref.data)
        ref = ref.next
    return -1 if len(stack) < k else stack[-k]


# TEST CASES
L = LinkedList()
print(kth_node_mid(L.construct([3, 4, 7, 5, 6, 16, 15, 61]), 3))  # 4
print(kth_node_mid(L.construct([1, 14, 6, 16, 4, 10]), 2))  # 14
print(kth_node_mid(L.construct([1, 14, 6, 16, 4, 10]), 10))  # -1
print(kth_node_mid(L.construct([1, 2, 3, 4]), 2))  # 1
print(kth_node_mid(L.construct([468, 335]), 1))  # 468
