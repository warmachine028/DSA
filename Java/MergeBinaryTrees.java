class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int data) {
        this.val = data;
    }

    TreeNode(int data, TreeNode left) {
        this(data);
        this.left = left;
    }

    TreeNode(int data, TreeNode left, TreeNode right) {
        this(data, left);
        this.right = right;
    }
}

class Solution {
    TreeNode add(TreeNode node1, TreeNode node2) {
        node1 = node1 != null ? node1 : new TreeNode(0);
        node2 = node2 != null ? node2 : new TreeNode(0);
        return new TreeNode(node1.val + node2.val);
    }

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null)
            return null;
        TreeNode node = add(t1, t2);
        node.left = mergeTrees(
                t1 != null ? t1.left : null,
                t2 != null ? t2.left : null);
        node.right = mergeTrees(
                t1 != null ? t1.right : null,
                t2 != null ? t2.right : null);
        return node;
    }
}

public class MergeBinaryTrees {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test Case 1
        TreeNode t1 = new TreeNode(1,
                new TreeNode(3,
                        new TreeNode(5),
                        null
                ),
                new TreeNode(2)
        );
        TreeNode t2 = new TreeNode(2,
                new TreeNode(1,
                        null,
                        new TreeNode(4)
                ),
                new TreeNode(3,
                        null,
                        new TreeNode(7)
                )
        );

        TreeNode result1 = solution.mergeTrees(t1, t2);
        printTree(result1);
        System.out.println();

        // Test Case 2
        TreeNode t3 = new TreeNode(1);
        TreeNode t4 = new TreeNode(1,
                null,
                new TreeNode(2));

        TreeNode result2 = solution.mergeTrees(t3, t4);
        printTree(result2);
    }

    // Helper method to print the binary tree in pre-order traversal
    private static void printTree(TreeNode node) {
        if (node == null)
            return;

        System.out.print(node.val + " ");
        printTree(node.left);
        printTree(node.right);
    }
}
