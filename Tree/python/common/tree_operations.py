class Tree:
    """Basic structure of a Tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Tree({})'.format(self.val)


def deserialize(string):
    """This creates a tree taking list as an input and returns root of the tree"""
    if string == '{}':
        return None
    nodes = [None if val == 'null' else Tree(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root