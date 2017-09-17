"""
671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead.

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5

Input:
    2
   / \
  2   2

Output: -1
"""

from Tree.python.common.tree_operations import deserialize


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        second_min_val = self.findSecondMinimumValueRecursive(root, root.val)
        if root.val == second_min_val:
            return -1
        else:
            return second_min_val

    def findSecondMinimumValueRecursive(self, root, current_val):
        if not root.left or not root.right or root.val > current_val:
            return root.val
        left = self.findSecondMinimumValueRecursive(root.left, root.val)
        right = self.findSecondMinimumValueRecursive(root.right, root.val)

        left_max = left if left != root.val else float('inf')
        right_max = right if right != root.val else float('inf')
        minimum = min(left_max, right_max)
        return minimum if minimum != float('inf') else root.val

sol = Solution()
print(sol.findSecondMinimumValue(deserialize('[2,2,5,2,2,null,null,2,2,6,5,2,2,2,2,2,2,2,2,5,4,2,2,2,2]')))
print(sol.findSecondMinimumValue(deserialize('[2,2,4,2,2,null,null,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2]')))
print(sol.findSecondMinimumValue(deserialize('[2,2,4,2,2,null,null,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2]')))
print(sol.findSecondMinimumValue(deserialize('[2,2,5,null,null,5,7]')))
print(sol.findSecondMinimumValue(deserialize('[2,2,2]')))
print(sol.findSecondMinimumValue(deserialize('[2]')))
