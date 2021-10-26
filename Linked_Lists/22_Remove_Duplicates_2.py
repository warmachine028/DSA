# CODE 22: Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from
# the original list.
#
# For example,
#
# Given 1->2->3->3->4->4->5, return 1->2->5.
#
# Given 1->1->1->2->3, return 2->3.

from SinglyLinkedList import Node, LinkedList


def remove_duplicate_sorted_2(head: Node) -> Node:
    temp = Node(0, head)
    prev = temp
    while head:
        if head.next and head.data == head.next.data:
            while head.next and head.data == head.next.data:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return temp.next


L = LinkedList()
print(remove_duplicate_sorted_2(L.construct([1, 1, 1, 2, 3, 4, 5])))  # 2 -> 3 -> 4 -> 5 -> NULL
print(remove_duplicate_sorted_2(L.construct([1, 1, 1, 1, 1])))  # NULL
print(remove_duplicate_sorted_2(L.construct([1])))  # 1 -> NULL
print(remove_duplicate_sorted_2(L.construct([1, 1, 2])))  # 2 -> NULL
print(remove_duplicate_sorted_2(L.construct([2, 1, 1])))  # 2 -> NULL
