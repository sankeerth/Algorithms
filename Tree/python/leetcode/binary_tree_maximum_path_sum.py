"""
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

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

Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
from Tree.python.common.tree_operations import deserialize, TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')
        
        def maxPathSumRecursive(root):
            nonlocal res
            if not root:
                return 0
            
            left = maxPathSumRecursive(root.left)
            right = maxPathSumRecursive(root.right)
            
            res = max(res, root.val, root.val+left+right, root.val+left, root.val+right)
            return max(root.val, root.val+left, root.val+right)
        
        maxPathSumRecursive(root)
        return res


sol = Solution()
print(sol.maxPathSum(deserialize("[-10,9,20,null,null,15,7]")))
print(sol.maxPathSum(deserialize("[1,2,3]")))
print(sol.maxPathSum(deserialize("[2,9,6,-1,-1]")))
