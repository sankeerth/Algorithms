"""
617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""

from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

sol = Solution()
print_levelorder_leetcode_style(sol.mergeTrees(deserialize('[1,3,2,5]'), deserialize('[2,1,3,null,4,null,7]')))
print_levelorder_leetcode_style(sol.mergeTrees(deserialize('[1]'), deserialize('[2,1,3,null,4,null,7]')))
print_levelorder_leetcode_style(sol.mergeTrees(deserialize('[1,3,2,5]'), deserialize('[2,1]')))

"""
My solution

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None or root2 is None:
            return root1 if root1 else root2
        
        root = TreeNode(root1.val+root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root
"""
