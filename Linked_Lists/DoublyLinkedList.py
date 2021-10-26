from typing import Optional

from Linked_Lists.SinglyLinkedList import Node as SinglyNode


class Node(SinglyNode):
    """ Basic Node Functions"""
    
    def __init__(self, data=0, nex=None, prev=None) -> None:
        super().__init__(data, nex)
        self.prev = prev
    
    def __str__(self, reverse=False):
        node = self.prev if reverse else self.next
        return f"Node[{self.data}] {f'<-> {node.__str__(reverse)}' if node else '-> NULL'}"


class DoublyLinkedList:
    """Basic Doubly LinkedList Functions """
    
    def __init__(self, items: Optional[list[int]] = None) -> None:
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        if not items: return
        for item in items:
            self.insert(item)
    
    def insert(self, data: int) -> Node:
        temp = Node(data, None, self.__tail)
        if not self.__head:
            self.__head = temp
        else:
            self.__tail.next = temp
        self.__tail = temp
        return self.head
    
    def rev_print(self) -> str:
        return self.__str__(True)
    
    def __str__(self, reverse=False):
        return (self.__tail if reverse else self.__head).__str__(reverse)
    
    @property
    def head(self):
        return self.__head


def main():
    d = DoublyLinkedList([1, 2, 3, 4, 5, 6])
    print(d)
    print(d.rev_print())
    print(Node(10, Node(90, Node(100, Node(1001)))).__str__())


# __main__
if __name__ == '__main__':
    main()
