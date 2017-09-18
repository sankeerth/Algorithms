"""
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels.
The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level,
where the null nodes between the end-nodes are also counted into the length calculation.

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
"""

from Tree.python.common.tree_operations import deserialize


class Solution(object):
    """Returns the max width of a binary tree"""
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        start_width_at_level = []
        self.max_width = -1

        def widthOfBinaryTreeRecursive(node, level, width):
            """
            Width of each level ranges from 1 to 2^level. Start width at each level is stored, first time a node is
            encountered at that level. Each time a node is encountered in the same level in subsequent time, max width is
            computed and stored.
            """
            if node:
                if level >= len(start_width_at_level):
                    start_width_at_level.append(width)
                if width - start_width_at_level[level] > self.max_width:
                    self.max_width = width - start_width_at_level[level]
                widthOfBinaryTreeRecursive(node.left, level+ 1, 2 * width - 1)
                widthOfBinaryTreeRecursive(node.right, level + 1, 2 * width)

        widthOfBinaryTreeRecursive(root, 0, 1)

        return self.max_width + 1

sol = Solution()
print(sol.widthOfBinaryTree(deserialize('[1,3,2,5,3,null,9]')))
print(sol.widthOfBinaryTree(deserialize('[1,3,2,5,null,null,9,6,null,null,7]')))
