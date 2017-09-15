from Tree.python.common.tree_operations import deserialize
from collections import deque


def level_order_traversal(root):
    """Level order tree traversal"""
    if not root:
        return
    q = deque()
    q.append(root)

    while q:
        root = q.popleft()
        print(root.val)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

level_order_traversal((deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]')))