"""
623. Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
"""
from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        def addOneRowRecursive(root, v, d, level):
            if root:
                if level == d - 1:
                    node_left = TreeNode(v)
                    node_left.left = root.left
                    root.left = node_left
                    node_right = TreeNode(v)
                    node_right.right = root.right
                    root.right = node_right
                else:
                    addOneRowRecursive(root.left, v, d, level + 1)
                    addOneRowRecursive(root.right, v, d, level + 1)

        if d == 1:
            node = TreeNode(v)
            node.left = root
            root = node
        else:
            addOneRowRecursive(root, v, d, 1)

        return root

sol = Solution()
print_levelorder_leetcode_style(sol.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 2))
print_levelorder_leetcode_style(sol.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 3))
print_levelorder_leetcode_style(sol.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 1))


"""
leetcode discuss solution:

def addOneRow(self, root, v, d):
    dummy, dummy.left = TreeNode(None), root
    row = [dummy]
    for _ in range(d - 1):
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    for node in row:
        node.left, node.left.left = TreeNode(v), node.left
        node.right, node.right.right = TreeNode(v), node.right
    return dummy.left
"""
