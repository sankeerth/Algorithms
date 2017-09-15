from Tree.python.common.tree_operations import deserialize


def non_recursive_inorder_traversal(root):
    """Non recursive in order tree traversal"""
    if not root:
        return
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left

        if not stack:
            return
        root = stack.pop()
        print(root.val)
        root = root.right

non_recursive_inorder_traversal(deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]'))