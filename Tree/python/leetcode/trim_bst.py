"""
669. Trim a Binary Search Tree

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2

Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""

from Tree.python.common.tree_operations import deserialize, print_levelorder_leetcode_style


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if low <= root.val <= high:
            return root
        
        return root.left if root.left else root.right


sol = Solution()
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 0, 2))
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 1, 6))
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 4, 4))
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 4, 7))
