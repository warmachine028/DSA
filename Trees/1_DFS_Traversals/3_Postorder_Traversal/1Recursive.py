# CODE 3a: Given the root of a binary tree, return the preorder traversal of its nodes' values.
from typing import Optional

from Trees.BinaryTree import TreeNode, BinaryTree


def postorder(root: TreeNode) -> list[Optional[int]]:
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []


# TEST_CASES
print(postorder(BinaryTree([1, 2, 3, 4, 5, 6]).root))  # [4, 5, 2, 6, 3, 1]
print(postorder(BinaryTree([1, None, 2]).root))  # [2, 1]
print(postorder(BinaryTree([]).root))  # []
