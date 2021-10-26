# CODE 10: Check if a Binary Tree is a valid one
from sys import maxsize

from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree, TreeNode


def valid_bst(root: TreeNode) -> bool:
    def check(node: TreeNode, min_bound: int, max_bound: int) -> bool:
        if not node: return True
        if node.data < min_bound or node.data > max_bound: return False
        return check(node.left, min_bound, node.data) and check(node.right, node.data, max_bound)

    return check(root, -maxsize, maxsize)
    # return True


print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), valid_bst(Tree.root))  # False
print((Tree := BinaryTree([2, 3, 4, 5, 6, 7, 8])), valid_bst(Tree.root))  # False

print((Tree := BinarySearchTree([1, None, 3, 4, 5, 6])), valid_bst(Tree.root))  # True
print((Tree := BinarySearchTree([5, 3, 7, 2, 4, 6, 8])), valid_bst(Tree.root))  # True
