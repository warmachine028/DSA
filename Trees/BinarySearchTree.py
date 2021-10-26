# CODE: Binary Search tree.

from typing import Any, Optional

from BinaryTree import BinaryTree, TreeNode


class BinarySearchTree(BinaryTree):
    def construct(self, arr: list[Any | None] | None) -> Optional['BinarySearchTree']:
        if not arr or arr[0] is None: return None
        root = TreeNode(arr[0])
        self._root = root
        for item in filter(lambda i: i is not None, arr[1:]):
            temp, ref = TreeNode(item), self._root
            while ref:
                if item < ref.data:
                    if not ref.left:
                        ref.left = temp
                        break
                    ref = ref.left
                else:
                    if not ref.right:
                        ref.right = temp
                        break
                    ref = ref.right
        return self


if __name__ == '__main__':
    def test(nodes: Optional[list[int | None]]) -> None:
        tree = BinarySearchTree(nodes)
        print(tree)
        print(tree.preorder_print())
        print("_______________________________________")


    with open('times.txt', 'w', encoding='utf-8') as f:
        test([])
        test([1])
        test([1, 2, 3])
        test([10000, 20000, 7, 99])
        test([1, 2])
        test([1, 2])
        test([1, 2, 3, 4])
        test([*range(12, -1, -1), *range(24, 12, -1)])
        Root = TreeNode(16,
                        TreeNode(12,
                                 TreeNode(10),
                                 TreeNode(13)
                                 ),
                        TreeNode(18,
                                 TreeNode(17),
                                 TreeNode(19)
                                 )
                        )
    print(BinarySearchTree().__str__(Root))

    """
            root
            ├──node1
            │  ├──node3
            │  │  └──node7
            │  │     ├──node8
            │  │     └──node9
            │  └──node4
            └──node2
               ├──node5
               └──node6
    """

    #     temp = TreeNode(arr[0])
    #     if not self.root:
    #         self.root = temp
    #         return
    #     ref = self.root
    #     while ref:
    #         if arr[0] < ref.data:
    #             if not ref.left:
    #                 ref.left = temp
    #                 break
    #             ref = ref.left
    #         else:
    #             if not ref.right:
    #                 ref.right = temp
    #                 break
    #             ref = ref.right
    #
    # def delete(self, data) -> None:
    #     if not self.root: return
    #     if self.root.data == data: self.root = self.__adopt_children(self.root)
    #     ref: TreeNode = self.root
    #     while ref:
    #         if data < ref.data:
    #             if ref.left and ref.left.data == data:
    #                 ref.left = self.__adopt_children(ref.left)
    #                 break
    #             ref = ref.left
    #         else:
    #             if ref.right and ref.right.data == data:
    #                 ref.right = self.__adopt_children(ref.right)
    #                 break
    #             ref = ref.right

    # @staticmethod
    # def __adopt_children(root: TreeNode) -> TreeNode:
    #     if not root.left: return root.right
    #     if not root.right: return root.left
    #     right_child = root.right
    #     last_right_child = (self := lambda node: self(node.right) if node.right else node)(root.left)
    #     last_right_child.right = right_child
    #     return root.left

    # @root.setter
    # def root(self, value):
    #     self._root = value
