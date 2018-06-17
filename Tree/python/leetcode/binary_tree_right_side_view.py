"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from Tree.python.common.tree_operations import deserialize


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()

        def preorder_from_right(root, level):
            if root:
                if len(result) <= level:
                    result.append(root.val)
                preorder_from_right(root.right, level+1)
                preorder_from_right(root.left, level+1)

        preorder_from_right(root, 0)
        return result


sol = Solution()
print(sol.rightSideView(deserialize("[[1,2,3,null,5,null,4]]")))
print(sol.rightSideView(deserialize("[1,2,null,4]")))
print(sol.rightSideView(deserialize("[1,2,3,4]")))
print(sol.rightSideView(deserialize("[1,2,3,4,5,null,null,null,6,7,null,8]")))
print(sol.rightSideView(deserialize("[null]")))
