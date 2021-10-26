# CODE 10a: Perform MergeSort on a Linked List using Recursion

from Linked_Lists.SinglyLinkedList import Node, LinkedList


def mid_finder(node: Node) -> Node:
    slow, fast = node, node.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def sort(head: Node) -> Node:
    if not head or not head.next: return head
    middle = mid_finder(head)
    head2 = middle.next
    middle.next = None
    left = sort(head)
    right = sort(head2)
    return merge(left, right)


# Recursive Approach
def merge(head1: Node, head2: Node) -> Node:
    if not head1: return head2
    if not head2: return head1
    
    if head1.data > head2.data:
        head2.next = merge(head1, head2.next)
        return head2
    
    head1.next = merge(head1.next, head2)
    return head1


L = LinkedList()
print(sort(L.construct([5, 4, 3, 8, 9, 0, -1, 9])))
print(sort(L.construct([99, 19])))
print(sort(L.construct([])))
print(sort(L.construct([0, 1, 2, 3, 4, 5, -1])))
