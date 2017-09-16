from Tree.python.common.tree_operations import deserialize


def find_max_binary_tree(root):
    """Computes the maximum value of a binary tree"""
    max_val = float('-inf')
    if root:
        left = find_max_binary_tree(root.left)
        right = find_max_binary_tree(root.right)
        max_val = left if left > right else right
        max_val = max_val if max_val > root.val else root.val

    return max_val

print(find_max_binary_tree(deserialize('[1,2,3,null,4,5,6,9,null,null,11,null,null,null,13]')))