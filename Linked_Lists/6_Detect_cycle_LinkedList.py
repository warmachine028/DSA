# CODE 6: Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a
# linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail 's next pointer is connected to. Note that pos is
# not passed as a parameter.
# Return true if there is a cycle in the linked list.Otherwise, return false.

# Example 1:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: true

# Example 2:
# Input: head = [1, 2], pos = 0
# Output: true

# Example 3:
# Input: head = [1], pos = -1
# Output: false

from SinglyLinkedList import Node, LinkedList


def detect_cycle(head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: return True
    return False


# __main__

class ModifiedLinkedList(LinkedList):
    def construct(self, items: list, pos=-1) -> Node:
        head = super().construct(items)
        if pos == -1:
            return head
        
        tail = head
        while tail.next:  # To reach end
            tail = tail.next
        node = head
        for i in range(pos):  # To reach ith index
            node = node.next
        
        # Setting tail.next to node
        tail.next = node
        return head


m = ModifiedLinkedList()
print(detect_cycle(m.construct([3, 2, 0, -4], 1)))  # True
print(detect_cycle(m.construct([3, 2, 0, -4], -1)))  # False
print(detect_cycle(m.construct([1, 2], 0)))  # True
print(detect_cycle(m.construct([1], -1)))  # False
print(detect_cycle(m.construct([1], 0)))  # True
