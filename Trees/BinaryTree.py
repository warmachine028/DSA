# Helper Function class for binary tree Programs
import math
from queue import Queue
from typing import Any, Optional


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.left: TreeNode = left
        self.data: Any = data
        self.right: TreeNode = right

    def __str__(self):
        """ print Immediate Children
        :return: return immediate children of the node
        """
        lines = [[str(self.data)],
                 [str(self.left.data) if self.left else None,
                  str(self.right.data) if self.right else None]]
        max_width = max(len(line) if line else 0 for line in (lines[0], *lines[1]))
        if max_width % 2: max_width += 1
        string_builder = ""
        per_piece = len(lines[-1]) * (max_width + 4)
        for i in range(len(lines)):
            line: list[str] = lines[i]
            hpw: int = int(math.floor(per_piece / 2) - 1)
            if i:
                for j in range(len(line)):
                    # Splitting into children
                    c: str = ' '
                    if j % 2:
                        if line[j - 1]:
                            c = '┴' if line[j] else '┘'
                        elif line[j]:
                            c = '└'
                    string_builder += c
                    # lines and Spaces
                    if line[j]:
                        for k in range(hpw):
                            string_builder += " " if j % 2 == 0 else "─"

                        string_builder += "┌" if j % 2 == 0 else "┐"

                        for k in range(hpw):
                            string_builder += "─" if j % 2 == 0 else " "

                        continue
                    string_builder += " " * (per_piece - 1)

                string_builder += '\n'

            # Printing the number
            for number in line:
                number: str = number or ""

                gap1 = int(math.ceil(per_piece / 2 - len(number) / 2))
                gap2 = int(math.floor(per_piece / 2 - len(number) / 2))

                # Printing a number with gap
                string_builder += f"{' ' * gap1}{number}{' ' * gap2}"

            string_builder += '\n'
            per_piece //= 2

        return string_builder


class BinaryTree:
    def __init__(self, items: list[Any] = None):
        self._root: Optional[TreeNode] = None
        self.construct(items)
        self.__string = None

    @property  # Made the root protected so that it cant be changed from outside
    def root(self):
        """Getter for protected variable root.
        :return: root node of the tree
        """
        return self._root

    # To construct a binary from an array level by level
    def construct(self, arr: list[Any | None] | None) -> Optional['BinaryTree']:
        """ Constructs Tree Level by level
        >>> BinTree = BinaryTree([1, 2, 3])
        
        >>> tree = BinaryTree(); tree.construct([1, 2, 3])
        BinaryTree.BinaryTree
        :param arr: Optional List of integers or None
        :return: BinaryTree.BinaryTree
        """
        if not arr or arr[0] is None: return None
        queue_: Queue[TreeNode] = Queue(maxsize=len(arr))
        root = TreeNode(arr[0])
        self._root = root
        queue_.put(root)
        current = 1
        while not queue_.empty() and current < len(arr):
            node = queue_.get()
            node.left = None if arr[current] is None else TreeNode(arr[current])
            if node.left:
                queue_.put(node.left)
            current += 1

            if current >= len(arr): break

            node.right = None if arr[current] is None else TreeNode(arr[current])
            if node.right:
                queue_.put(node.right)
            current += 1
        return self

    # Helper function for pre_order_traversal

    # Pre Order Tree Traversal
    def preorder_print(self, root: TreeNode = None):
        """ Pre Order Tree Traversal
        >>> BinTree = BinaryTree([1, 2, 3])
        >>> print(BinTree.preorder_print())
        <BLANKLINE>
        1 <- root
        ├── 2
        └── 3
        
        >>> tree = BinaryTree(); print(tree.preorder_print(BinTree.root))
        NULL <- root
        
        :param root: if not passed or None passed, then checks for self.root
        :return: returns "NULL" if invalid root was given else a Pre order Tree Representation
        """

        def build_string(root_: TreeNode, has_right_child: bool, padding="", pointer="") -> None:
            if not root_: return
            self.__string += f"\n{padding}{pointer}{root_.data}{' <- root' if root_ is self.root else ''}"
            if root_ != self.root: padding += "│  " if has_right_child else "   "
            left_pointer, right_pointer = "├── " if root_.right else "└── ", "└── "
            build_string(root_.left, bool(root_.right), padding, left_pointer)
            build_string(root_.right, False, padding, right_pointer)

        if not root: root = self._root
        if not self.root: return "NULL <- root"
        self.__string = ""
        build_string(root, bool(self.root.right) if self.root.right else False)
        return self.__string

    # Level Order Tree Traversal
    def __str__(self, root: TreeNode = None):
        """Level Order Tree Traversal
        >>> BinTree = BinaryTree([1, 2, 3])
        >>> print(BinTree)
        ... # doctest: +NORMALIZE_WHITESPACE
              1
           ┌──┴──┐
           2     3

        >>> print(BinaryTree().__str__(BinTree.root))
        ... # doctest: +NORMALIZE_WHITESPACE
              1
           ┌──┴──┐
           2     3

        :param root: if not passed or None passed, then checks for self.root
        :return: returns "NULL" if invalid root was given else a Level order Tree Representation
        """
        if not root: root = self._root
        if not root: return "  NULL\n"
        lines: list[list[str]] = []
        level: list[TreeNode] = [root]
        number_of_nodes: int = 1
        max_width: int = 0
        while number_of_nodes:
            line: list[Optional[str]] = []
            next_level: list[Optional[TreeNode]] = []
            number_of_nodes = 0
            for node in level:
                if node:
                    data = str(node.data)
                    max_width = max(len(data), max_width)
                    line.append(data)
                    next_level += [node.left, node.right]
                    if node.left: number_of_nodes += 1
                    if node.right: number_of_nodes += 1
                    continue
                line.append(None)
                next_level += [None] * 2
            if max_width % 2: max_width += 1
            lines.append(line)
            level = next_level
        
        per_piece = len(lines[-1]) * (max_width + 4)
        string_builder = f"{' ' * int(math.ceil(per_piece / 2 - len(lines[0]) / 2))}" \
                         f"{lines[0][0]}" \
                         f"{' ' * int(math.floor(per_piece / 2 - len(lines[0]) / 2))}\n"

        per_piece //= 2
        for i, line in enumerate(lines[1:], 1):
            hpw: int = int(math.floor(per_piece / 2) - 1)
            # Printing the lines
            for j, num in enumerate(line):
                # Splittings
                string_builder += (('┴' if num else '┘') if line[j - 1] else '└' if num else ' ') if j % 2 else ' '

                # lines and Spaces
                if not num:
                    string_builder += ' ' * (per_piece - 1)
                    continue
                string_builder += f"{'─' * hpw}┐{' ' * hpw}" if j % 2 else f"{' ' * hpw}┌{'─' * hpw}"
            string_builder += '\n'

            # Printing the number
            for num in line:
                num: str = num or ''
                gap1 = int(math.ceil(per_piece / 2 - len(num) / 2))  # gap1
                gap2 = int(math.floor(per_piece / 2 - len(num) / 2))  # gap2
                string_builder += f"{' ' * gap1}{num}{' ' * gap2}"
            string_builder += '\n'
            per_piece //= 2

        return string_builder


if __name__ == '__main__':
    def test(nodes: Optional[list[int | None]]) -> None:
        tree = BinaryTree(nodes)
        print(tree)
        print(tree.preorder_print())
        print("_____")


    test([])
    test([1])
    test([1, 2, 3])
    test([10000, 20000, 7, 99])
    test([1, 2])
    test([1, None, 2])
    test([*range(1, 2 ** 5)])
    test([1, None, 2, None, 3, None, 4])
    ROOT = TreeNode(16,
                    TreeNode(4,
                             TreeNode(2),
                             TreeNode(2)
                             ),
                    TreeNode(4,
                             TreeNode(2),
                             TreeNode(2)
                             )
                    )
    print(BinaryTree().__str__(ROOT))
