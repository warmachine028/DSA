# CODE 8: Write a function to delete a node in a singly-linked list. You will not be given access to the head of the
# list, instead you will be given access to the node to be deleted directly.
#
# NOTE: It is guaranteed that the node to be deleted is not a tail node in the list.
from typing import Optional

from SinglyLinkedList import Node, LinkedList


def delete_node(node: Node) -> None:
    node.data = node.next.data
    node.next = node.next.next


# __main__
def get_node(head: Node, data: int) -> Optional[Node]:
    while head:
        if head.data == data:
            return head
        head = head.next
    return None


L = LinkedList()
Head = L.construct([1, 2, 3, 4, 5, 6])
delete_node(get_node(Head, 4))
print(Head)
