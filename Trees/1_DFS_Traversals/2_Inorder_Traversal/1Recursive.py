# CODE 2a: Given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional

from Trees.BinaryTree import TreeNode, BinaryTree


def inorder(root: Optional[TreeNode]) -> list[Optional[int]]:
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []


# TEST_CASE
print(inorder(BinaryTree([1, None, 2]).root))  # [1, 2]
print(inorder(BinaryTree([1, 2]).root))  # [2, 1]
print(inorder(BinaryTree([]).root))  # []
