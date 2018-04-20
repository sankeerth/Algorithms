"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
"""


from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodes = list()

        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root.val)
                inorder(root.right)

        inorder(root)

        low, high = 0, 0
        for i in range(1, len(nodes)):
            if nodes[i] < nodes[i - 1]:
                low = i - 1
                break

        for i in range(len(nodes) - 2, -1, -1):
            if nodes[i] > nodes[i + 1]:
                high = i + 1
                break

        def inorder_replace(root):
            if root:
                inorder_replace(root.left)
                if self.count == low:
                    root.val = nodes[high]
                elif self.count == high:
                    root.val = nodes[low]
                self.count += 1
                inorder_replace(root.right)

        self.count = 0
        inorder_replace(root)
        return root


sol = Solution()
print_levelorder_leetcode_style(sol.recoverTree(deserialize('[1,3,null,null,2]')))
print_levelorder_leetcode_style(sol.recoverTree(deserialize('[3,1,4,null,null,2]')))
