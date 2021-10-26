# CODE 6a: Given a binary tree, find its minimum depth.
#
# The minimum depth of a binary tree is the number of nodes along the longest path from the root node down to the
# farthest leaf node.
#
# NOTE : The path has to end on a leaf node.

from Trees.BinaryTree import BinaryTree, TreeNode


def min_depth(root: TreeNode) -> int:
    if not root: return 0
    heights = min_depth(root.left), min_depth(root.right)
    return 1 + (min(heights) if not all(heights) else max(heights))


# TEST_CASES
print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), min_depth(Tree.root))  # 1
print((Tree := BinaryTree([1, 2])), min_depth(Tree.root))  # 1
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), min_depth(Tree.root))  # 3
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, 7, None, *[None] * 5, 10])), min_depth(Tree.root))  # 4
