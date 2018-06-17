"""
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""
from Tree.python.common.tree_operations import deserialize


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0

        def postorder(root):
            nonlocal result
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)

            count = 1
            if root.left and root.left.val == root.val + 1:
                count = max(count, left+1)
            if root.right and root.right.val == root.val + 1:
                count = max(count, right+1)
            result = max(result, count)
            return count

        postorder(root)

        return result


sol = Solution()
print(sol.longestConsecutive(deserialize("[1,null,3,2,4,null,null,null,5]")))
print(sol.longestConsecutive(deserialize("[2,null,3,2,null,1]")))
print(sol.longestConsecutive(deserialize("[1,null,2,3,3,null,4,null,4,null,null,5]")))
print(sol.longestConsecutive(deserialize("[1,null,2,3,4,null,4,null,5,null,null,6,null,7,7,null,8,8,null,null,null,null,9]")))
print(sol.longestConsecutive(deserialize("[null]")))
