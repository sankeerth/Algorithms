"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import List
from Tree.python.common.tree_operations import deserialize, TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, level):
            if root:
                if len(res) == level:
                    res.append(root.val)
                dfs(root.right, level+1)
                dfs(root.left, level+1)
        
        dfs(root, 0)
        return res


sol = Solution()
print(sol.rightSideView(deserialize("[[1,2,3,null,5,null,4]]")))
print(sol.rightSideView(deserialize("[1,2,null,4]")))
print(sol.rightSideView(deserialize("[1,2,3,4]")))
print(sol.rightSideView(deserialize("[1,2,3,4,5,null,null,null,6,7,null,8]")))
print(sol.rightSideView(deserialize("[null]")))
