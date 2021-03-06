from Tree.python.common.tree_operations import deserialize


def find_element_binary_tree(root, data):
    """Returns true if an element is found in the binary tree else false"""
    found = False
    if root:
        if root.val == data:
            return True
        found = find_element_binary_tree(root.left, data)
        if not found:
            found = find_element_binary_tree(root.right, data)

    return found


"""
Alternative and simpler solution

def find_element_binary_tree(root, data):
    if root:
        if root.val == data:
            return True
        return find(root.left, data) or find(root.right, data)
    return False
"""


print(find_element_binary_tree(deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]'), 5))
print(find_element_binary_tree(deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]'), 6))
print(find_element_binary_tree(deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]'), 10))
print(find_element_binary_tree(deserialize('[1,2,3,null,4,5,6,7,null,null,8,null,null,null,9]'), 0))
