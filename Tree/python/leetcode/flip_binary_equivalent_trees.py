"""
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.

Example 1:
Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Example 4:
Input: root1 = [0,null,1], root2 = []
Output: false

Example 5:
Input: root1 = [0,null,1], root2 = [0,1]
Output: true

Constraints:
The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
"""
from common.tree_operations import TreeNode, deserialize


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def flipEquivRecursive(root1, root2):
            if not root1 and not root2:
                return True
            
            if root1 and not root2 or root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False

            flipLeft = root1.left and root2.right and root1.left.val == root2.right.val
            flipRight = root1.right and root2.left and root1.right.val == root2.left.val

            if flipLeft or flipRight:
                return flipEquivRecursive(root1.left, root2.right) and flipEquivRecursive(root1.right, root2.left)
            else:
                return flipEquivRecursive(root1.left, root2.left) and flipEquivRecursive(root1.right, root2.right)
        
        return flipEquivRecursive(root1, root2)


sol = Solution()
print(sol.flipEquiv(deserialize('[1,2,3,4,5,6,null,null,null,7,8]'), deserialize('[1,3,2,null,6,4,5,null,null,null,null,8,7]')))
# failed testcase
print(sol.flipEquiv(deserialize('[1,2,3,4,5,6,null,null,null,7,8]'), deserialize('[99,3,2,null,6,4,5,null,null,null,null,8,7]')))


"""
Leetcode solution:

class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        List<Integer> vals1 = new ArrayList();
        List<Integer> vals2 = new ArrayList();
        dfs(root1, vals1);
        dfs(root2, vals2);
        return vals1.equals(vals2);
    }

    public void dfs(TreeNode node, List<Integer> vals) {
        if (node != null) {
            vals.add(node.val);
            int L = node.left != null ? node.left.val : -1;
            int R = node.right != null ? node.right.val : -1;

            if (L < R) {
                dfs(node.left, vals);
                dfs(node.right, vals);
            } else {
                dfs(node.right, vals);
                dfs(node.left, vals);
            }

            vals.add(null);
        }
    }
}
"""
