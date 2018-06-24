"""
116. Populating Next Right Pointers in Each Node

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
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
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
    def connect(self, root):
        if root:
            if root.left:
                root.left.next = root.right
            if root.right and root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root


sol = Solution()
print_levelorder_leetcode_style(sol.connect(deserialize("[1, 2, 3, 4, 5, 6, 7]")))


"""
Another solution:

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root, parent=None, right=False):
        if root:
            if right and parent.next:
                root.next = parent.next.left
            if root.left:
                root.left.next = root.right
            self.connect(root.left, root, False)
            self.connect(root.right, root, True)

        return root
"""