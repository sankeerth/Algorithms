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
    def __init__(self):
        self.max_width = None

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

        def widthOfBinaryTreeRecursiveII(node, width):
            """
            This is a much simpler solution than the previous one as there is not no need for the list.
            Logic is the same that node in each level ranges from 1 to 2^level and that is sufficient
            to come up with a solution by having a max_val variable
            :param node: TreeNode
            :param width: int
            :return: int
            """

            if node:
                self.max_width = max(self.max_width, width)
                widthOfBinaryTreeRecursiveII(node.left, width*2 - 1)
                widthOfBinaryTreeRecursiveII(node.right, width*2)

        def widthOfBinaryTreeIterative(node):
            """
            Iterative approach using level order traversal
            :param root: TreeNode
            :return: int
            """
            def calc(q):
                l = len(q)
                for i in range(l - 1, -1, -1):
                    if q[i] is not None:
                        break
                    l -= 1
                return l

            if not node:
                return 0

            q = list()
            q.append(node)
            q.append('end_level')
            max_val = 1

            while q:
                node = q.pop(0)
                if node == 'end_level':
                    l = calc(q)
                    if l is 0:
                        break
                    max_val = max(max_val, l)
                    q.append('end_level')
                    continue
                q.append(node.left if root else None)
                q.append(node.right if root else None)

            return max_val


        # widthOfBinaryTreeRecursive(root, 0, 1)
        # return self.max_width + 1

        # return widthOfBinaryTreeIterative(root)

        widthOfBinaryTreeRecursiveII(root, 1)
        return self.max_width


sol = Solution()
print(sol.widthOfBinaryTree(deserialize('[1,3,2,5,3,null,9]')))
print(sol.widthOfBinaryTree(deserialize('[1,3,2,5,null,null,9,6,null,null,7]')))
print(sol.widthOfBinaryTree(deserialize('[1,3,2,5,3,9,null]')))




