"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
from Tree.python.common.tree_operations import TreeNode, deserialize


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        self.traverse_left_until_left(root)

    def traverse_left_until_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        self.stack.pop()
        self.traverse_left_until_left(top.right)
        return top.val


root = deserialize("[4,2,5,1,3,null,7]")
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print(v)

root = deserialize("[9,4,null,3,7,2,null,5,null,1,null,null,6]")
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print(v)