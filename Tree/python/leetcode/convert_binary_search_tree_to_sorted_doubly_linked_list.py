"""
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor and successor pointers 
in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element 
is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the 
tree node should point to its predecessor, and the right pointer should point to its successor. 
You should return the pointer to the smallest element of the linked list.

Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:
Input: root = [2,1,3]
Output: [1,2,3]

Example 3:
Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.

Example 4:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
"""
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


def print_dll_style(root):
    r1 = root
    leftToRight, rightToLeft = [], []
    
    while True:
        leftToRight.append(r1.val)
        r1 = r1.right
        if r1 == root:
            break
    
    r1 = root.left
    while True:
        rightToLeft.append(r1.val)
        r1 = r1.left
        if r1 == root.left:
            break
    print(leftToRight, rightToLeft)


class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        def treeToDLL(root):
            if not root.left and not root.right:
                return root, root
            
            leftSubtreeLeftMost, rightSubtreeRightMost = root, root
            if root.left:
                leftSubtreeLeftMost, leftSubtreeRightMost = treeToDLL(root.left)
                leftSubtreeRightMost.right = root
                root.left = leftSubtreeRightMost
            
            if root.right:
                rightSubtreeLeftMost, rightSubtreeRightMost = treeToDLL(root.right)
                rightSubtreeLeftMost.left = root
                root.right = rightSubtreeLeftMost

            return leftSubtreeLeftMost, rightSubtreeRightMost

        head, tail = treeToDLL(root)
        head.left = tail
        tail.right = head
        return head


sol = Solution()
print_dll_style(sol.treeToDoublyList(deserialize('[2,1,3]')))
print_dll_style(sol.treeToDoublyList(deserialize('[4,2,5,1,3]')))
print_dll_style(sol.treeToDoublyList(deserialize('[6,4,7,2,5,null,null,1,3]')))
print_dll_style(sol.treeToDoublyList(deserialize('[6,4,null,2,5,1,3]')))


"""
Leetcode solution:
Standard inorder recursion follows left -> node -> right order, where left and right parts 
are the recursion calls and node part is where all processing is done.

Processing here is basically to link the previous node with the current one, and because of 
that one has to track the last node which is the largest node in a new doubly linked list so far.

One more detail : one has to keep the first, or the smallest, node as well to close the ring of doubly linked list.

Here is the algorithm :

Initiate the first and the last nodes as nulls.
Call the standard inorder recursion helper(root) :
    If node is not null :
        Call the recursion for the left subtree helper(node.left).
        If the last node is not null, link the last and the current node nodes.
        Else initiate the first node.
        Mark the current node as the last one : last = node.
        Call the recursion for the right subtree helper(node.right).
Link the first and the last nodes to close DLL ring and then return the first node.


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            '''
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            '''
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first
"""
