# CODE 5a: Given a binary tree, find its maximum depth.
#
# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the
# farthest leaf node.
#
# NOTE : The path has to end on a leaf node.

from Trees.BinaryTree import BinaryTree, TreeNode


def max_depth(root: TreeNode) -> int:
    if not root: return 0
    height_of_root = 1
    height_of_left_sub_tree = max_depth(root.left)
    height_of_right_sub_tree = max_depth(root.right)
    return height_of_root + max(height_of_left_sub_tree, height_of_right_sub_tree)


# TEST_CASES
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), max_depth(Tree.root))  # 3
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, 7, None, *[None] * 5, 10])), max_depth(Tree.root))  # 4
