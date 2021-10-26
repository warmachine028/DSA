# CODE 5b: Given a binary tree, find its maximum depth.
#
# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the
# farthest leaf node.
#
# NOTE : The path has to end on a leaf node.

from Trees.BinaryTree import BinaryTree, TreeNode


def max_depth(root: TreeNode) -> int:
    return 1 + max(max_depth(root.left), max_depth(root.right)) if root else 0


# TEST_CASES
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), max_depth(Tree.root))  # 3
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, 7, None, *[None] * 5, 10])), max_depth(Tree.root))  # 4
