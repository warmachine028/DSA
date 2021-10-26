# CODE 5: You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
#
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

from SinglyLinkedList import Node, LinkedList


def add(head1: Node, head2: Node) -> Node:
    carry = 0
    ref = head = None
    
    while head1 or head2 or carry:
        int1 = head1.data if head1 else 0
        int2 = head2.data if head2 else 0
        
        carry, summa = divmod(int1 + int2 + carry, 10)
        
        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None
        if not head:
            ref = head = Node(summa)
        else:
            ref.next = Node(summa)
            ref = ref.next
    return head


# TESTCASES
L = LinkedList()
print(add(L.construct([1, 1, 2]), L.construct([1, 2, 3])))  # 2 -> 3 -> 5
print(add(L.construct([1, 1, 2, 3, 3]), L.construct([1, 2, 3])))  # 2 -> 3 -> 5 -> 3 -> 3
print(add(L.construct([1]), L.construct([1, 2, 3])))  # 2 -> 2 -> 3

# (2 -> 4 -> 3) + (5 -> 6 -> 4)
print(add(L.construct([2, 4, 3]), L.construct([5, 6, 4])))  # 7 -> 0 -> 8
print(add(L.construct([9, 9, 1]), L.construct([1])))  # 0 -> 0 -> 2
print(add(L.construct([9, 9, 9]), L.construct([1])))  # 0 -> 0 -> 0 -> 1
