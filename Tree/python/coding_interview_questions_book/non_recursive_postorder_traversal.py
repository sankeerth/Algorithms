from Tree.python.common.tree_operations import deserialize


def non_recursive_postorder_traversal(root):
    """Non recursive post order tree traversal"""
    if not root:
        return
    stack = []
    while True:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        if not stack:
            return
        root = stack.pop()

        top = stack[-1] if stack else None
        if root.right == top:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.val)
            root = None

non_recursive_postorder_traversal(deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]'))