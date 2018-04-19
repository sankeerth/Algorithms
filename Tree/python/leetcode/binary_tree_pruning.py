"""
814. Binary Tree Pruning

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

---> See figure in the problem

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

---> See figure in the problem

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

---> See figure in the problem

"""

from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if not root.left and not root.right and root.val is 0:
                return None
        return root


sol = Solution()
print_levelorder_leetcode_style(sol.pruneTree(deserialize('[1,null,0,0,1]')))
print_levelorder_leetcode_style(sol.pruneTree(deserialize('[1,0,1,0,0,0,1]')))
print_levelorder_leetcode_style(sol.pruneTree(deserialize('[1,1,0,1,1,0,1,0]')))
