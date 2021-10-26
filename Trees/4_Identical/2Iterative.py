# CODE 4b: Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

from queue import Queue

from Trees.BinaryTree import TreeNode, BinaryTree


# Using Level Order Traversal / BFS
def is_same_tree(root1: TreeNode, root2: TreeNode) -> bool:
    if not any([root1, root2]): return True  # True if both trees are empty
    if not all([root1, root2]): return False  # False if either of the tree is Empty

    queue1 = Queue()  # To Traverse root1
    queue2 = Queue()  # To Traverse root2

    queue1.put(root1), queue2.put(root2)

    while not queue1.empty() and not queue2.empty():
        root1, root2 = queue1.get(), queue2.get()
        if root1.data != root2.data: return False

        left1, left2 = root1.left, root2.left
        if any([left1, left2]) and not all([left1, left2]): return False
        if all([left1, left2]):  # Enqueue left children of both nodes
            queue1.put(left1)
            queue2.put(left2)

        right1, right2 = root1.right, root2.right
        if any([right1, right2]) and not all([right1, right2]): return False
        if all([right1, right2]):  # Enqueue right children of both nodes
            queue1.put(right1)
            queue2.put(right2)

    return True


print(is_same_tree(BinaryTree([1, 2, 3, 4, 5]).root, BinaryTree([1, 2, 3, 4, 5]).root))  # True
print(is_same_tree(BinaryTree([1]).root, BinaryTree([1]).root))  # True
print(is_same_tree(BinaryTree([]).root, BinaryTree([]).root))  # True

print(is_same_tree(BinaryTree([1, 2, 3, 4, 5]).root, BinaryTree([1, 2, 3, 4]).root))  # False
print(is_same_tree(BinaryTree([2, 1]).root, BinaryTree([1, 2]).root))  # False
print(is_same_tree(BinaryTree([]).root, BinaryTree([1]).root))  # False
