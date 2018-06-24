"""
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
"""

from Tree.python.common.tree_operations import print_levelorder_leetcode_style


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def deserialize(string):
    """This creates a tree taking list as an input and returns root of the tree"""
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeLinkNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_sibling(self, root):
        sibling = root.next
        while sibling:
            if sibling.left:
                return sibling.left
            if sibling.right:
                return sibling.right
            sibling = sibling.next
        return None

    def connect(self, root):
        if root:
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = self.connect_sibling(root)

            if root.right:
                root.right.next = self.connect_sibling(root)
            self.connect(root.right)  # Right subtree has to be solved first else it fails for the last test case
            self.connect(root.left)


sol = Solution()
print_levelorder_leetcode_style(sol.connect(deserialize("[1, 2, 3, 4, 5, 6, 7]")))
print_levelorder_leetcode_style(sol.connect(deserialize("[1,2,3,4,null,5,6,7,null,null,8,null,9,null,10,null,null,11,null]")))
print_levelorder_leetcode_style(sol.connect(deserialize("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]")))
