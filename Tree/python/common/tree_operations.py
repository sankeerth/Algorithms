from collections import deque


class TreeNode:
    """Basic structure of a Tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    """This creates a tree taking list as an input and returns root of the tree"""
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def print_levelorder_leetcode_style(root):
    if not root:
        return '[]'

    stack = []
    q = deque()
    q.append(root)

    while q:
        root = q.popleft()
        if not root:
            stack.append(None)
        else:
            stack.append(str(root.val))
            q.append(root.left)
            q.append(root.right)
        stack.append(',')

    print('[', end='', flush=True)
    for item in stack[:-1]:
        if item is None:
            print('null', end='', flush=True)
        else:
            print(item, end='', flush=True)
    print(']', end='', flush=True)
    print()
