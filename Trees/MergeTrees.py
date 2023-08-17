from datastax.Nodes import TreeNode
from datastax.Trees import BinaryTree


def mergeTrees(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
    if not any((root1, root2)):
        return None
    root1 = root1 or TreeNode(0)
    root2 = root2 or TreeNode(0)
    root = TreeNode(root1.data + root2.data)
    root.set_left(mergeTrees(root1.left, root2.left))
    root.set_right(mergeTrees(root1.right, root2.right))
    return root


t1 = BinaryTree([1, 2, 4, 3, 9, 10])
t2 = BinaryTree([1, None, 3, 10, 8, 8])

print(t1, t2, sep="\n")
print(BinaryTree(root=mergeTrees(t1.root, t2.root)))
print(BinaryTree(root=mergeTrees(t1.root, None)))
