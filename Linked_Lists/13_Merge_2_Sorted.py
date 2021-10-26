# CODE 13: Merge 2 sorted Linked_Lists

from SinglyLinkedList import Node, LinkedList


def merge(head1: Node, head2: Node) -> Node:
    if not head1: return head2
    if not head2: return head1
    
    if head1.data > head2.data:
        head = head2
        head2 = head2.next
    else:
        head = head1
        head1 = head1.next
    
    ref = head
    while head1 and head2:
        if head1.data > head2.data:
            ref.next = head2
            head2 = head2.next
        else:
            ref.next = head1
            head1 = head1.next
        ref = ref.next
    ref.next = head2 or head1
    return head


L = LinkedList()
newList = merge(L.construct([1, 2, 3]), L.construct([3, 4, 5]))
print(newList)
