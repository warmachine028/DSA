# CODE 3: Given a Binary Tree A containing N nodes. You need to find the path from Root to a given node B.
#
# NOTE:
# No two nodes in the tree have same data values.
# You can assume that B is present in the tree A and a path always exists.
from Trees.BinaryTree import BinaryTree, TreeNode


# Using Inorder Traversal
def find_path(root: TreeNode, data: int) -> list[int]:
    result: list[int] = []

    # Using BackTracking
    def path(node) -> bool:
        if not node: return False
        result.append(node.data)
        if path(node.left) or node.data == data or path(node.right): return True
        result.pop()
        # return False

    path(root)
    return result


# TEST_CASE
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), find_path(Tree.root, 3))  # [1, 3]
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), find_path(Tree.root, 5))  # [1, 2, 5]
print((Tree := BinaryTree([1])), find_path(Tree.root, 1))  # [1]
print((Tree := BinaryTree([])), find_path(Tree.root, 0))  # []
print((Tree := BinaryTree([1, 2, 3, 4, 5, *[None] * 4, 6, 7])), find_path(Tree.root, 5))  # [1, 2, 5, 7]


def find_path(root: TreeNode, data: int) -> list[int | None]:
    path = []

    def find(node) -> bool:
        if not node: return False
        path.append(node.data)
        if find(node.left) or node.data == data or find(node.right): return True
        path.pop()

    find(root)
    return path


# TEST_CASE
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), find_path(Tree.root, 3))  # [1, 3]
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), find_path(Tree.root, 5))  # [1, 2, 5]
print((Tree := BinaryTree([1])), find_path(Tree.root, 1))  # [1]
print((Tree := BinaryTree([])), find_path(Tree.root, 0))  # []
print((Tree := BinaryTree([1, 2, 3, 4, 5, *[None] * 4, 6, 7])), find_path(Tree.root, 5))  # [1, 2, 5, 7]
