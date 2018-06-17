"""
449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same
or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if root:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)

        res = list()
        preorder(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        left = float('-inf')
        right = float('inf')
        data = [int(val) for val in data.strip('[]{}').split(',')]
        length = len(data)
        index = 0

        def build_bst(left, right):
            nonlocal index

            if index >= length:
                return None
            node = TreeNode(data[index])
            if index + 1 < length and left < data[index + 1] < node.val:
                index += 1
                node.left = build_bst(left, node.val)
            if index + 1 < length and node.val < data[index + 1] < right:
                index += 1
                node.right = build_bst(node.val, right)

            return node

        return build_bst(left, right)


codec = Codec()
codec.serialize(codec.deserialize("[2,1,3]"))


'''
leetcode discuss solution:

class Codec:

    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        vals = []
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        preorder = [int(val) for val in data.strip('[]{}').split(',')]
        inorder = sorted(preorder)
        return self.buildTree(preorder[::-1], inorder[::-1])

    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        return build(None)


codec = Codec()
codec.serialize(codec.deserialize("[2,1,3]"))
'''
