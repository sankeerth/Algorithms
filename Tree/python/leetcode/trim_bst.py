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


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trimBSTRecursive(node):
            if node:
                if L <= node.val <= R:
                    node.left = trimBSTRecursive(node.left)
                    node.right = trimBSTRecursive(node.right)
                else:
                    if node.val < L:
                        return trimBSTRecursive(node.right)
                    else:
                        return trimBSTRecursive(node.left)
                return node

        return trimBSTRecursive(root)

sol = Solution()
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 0, 2))
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 1, 6))
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 4, 4))
print_levelorder_leetcode_style(sol.trimBST(deserialize('[3,0,4,null,2,5,7,1,null,null,6]'), 4, 7))
