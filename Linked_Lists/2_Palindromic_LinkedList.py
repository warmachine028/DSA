# CODE 12: Find whether a linked list is palindrome or not

from SinglyLinkedList import LinkedList, Node


def mid_finder(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse(head: Node) -> Node:
    curr, prev = head, None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev


def check_palindrome(head: Node) -> bool:
    if head is None:
        return False
    
    tail = reverse(mid_finder(head))
    while head and tail:
        if head.data != tail.data:
            return False
        head = head.next
        tail = tail.next
    return True


L = LinkedList()
print(check_palindrome(L.construct([1, 2, 3, 2, 1])))  # True
print(check_palindrome(L.construct([1, 2, 1, 1])))  # False

actual = L.construct([1, 2, 3, 4, 5, 6])  # False
print(check_palindrome(actual))  # False

actual = L.construct([1, 2, 2, 1])
print(check_palindrome(actual))  # True

actual = L.construct([1, 2, 1])
print(check_palindrome(actual))  # True

actual = L.construct([1, 7, 0, 7, 1])
print(check_palindrome(actual))  # True

actual = L.construct([1, 2])
print(check_palindrome(actual))  # False

actual = L.construct([])
print(check_palindrome(actual))  # False
