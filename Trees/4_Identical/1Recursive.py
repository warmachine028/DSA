# CODE 4a: Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


from Trees.BinaryTree import BinaryTree, TreeNode


# sys.path.append(r'D:\Python_Programs\Competitive Programming\Trees')


def is_same_tree(root1: TreeNode, root2: TreeNode) -> bool:
    if not any([root1, root2]): return True
    if not all([root1, root2]) or root1.data != root2.data: return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)


print(is_same_tree(BinaryTree([1, 2, 3, 4, 5]).root, BinaryTree([1, 2, 3, 4, 5]).root))  # True
print(is_same_tree(BinaryTree([1]).root, BinaryTree([1]).root))  # True
print(is_same_tree(BinaryTree([]).root, BinaryTree([]).root))  # True
print(is_same_tree(BinaryTree([1, None, 2]).root, BinaryTree([1, None, 2]).root))  # True

print(is_same_tree(BinaryTree([1, 2, 3, 4, 5]).root, BinaryTree([1, 2, 3, 4]).root))  # False
print(is_same_tree(BinaryTree([2, 1]).root, BinaryTree([1, 2]).root))  # False
print(is_same_tree(BinaryTree([]).root, BinaryTree([1]).root))  # False
print(is_same_tree(BinaryTree([1, None, 3, 4]).root, BinaryTree([1, 3, None, 4]).root))  # False
