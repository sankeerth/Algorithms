"""
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
from Tree.python.common.tree_operations import deserialize


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = float('-inf')

        def max_sum(root):
            nonlocal result
            if not root:
                return 0
            left = max_sum(root.left)
            right = max_sum(root.right)
            result = max(result, root.val, (left + right + root.val), (left + root.val), (right + root.val))
            return max((left + root.val), (right + root.val), root.val)

        max_sum(root)
        return result


sol = Solution()
print(sol.maxPathSum(deserialize("[-10,9,20,null,null,15,7]")))
print(sol.maxPathSum(deserialize("[1,2,3]")))
print(sol.maxPathSum(deserialize("[2,9,6,-1,-1]")))
