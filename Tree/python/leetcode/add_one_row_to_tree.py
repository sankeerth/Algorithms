"""
623. Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
"""
from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def addOneRowRec(root, curDepth):
            if not root:
                return
            
            if curDepth == depth-1:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
                return
            
            addOneRowRec(root.left, curDepth+1)
            addOneRowRec(root.right, curDepth+1)
        
        if not root:
            return root
        
        if depth == 1:
            newRoot = TreeNode(val, root, None)
            return newRoot
        
        addOneRowRec(root, 1)
        return root


sol = Solution()
print_levelorder_leetcode_style(sol.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 2))
print_levelorder_leetcode_style(sol.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 3))
print_levelorder_leetcode_style(sol.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 1))


"""
leetcode discuss solution:

def addOneRow(self, root, v, d):
    dummy, dummy.left = TreeNode(None), root
    row = [dummy]
    for _ in range(d - 1):
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    for node in row:
        node.left, node.left.left = TreeNode(v), node.left
        node.right, node.right.right = TreeNode(v), node.right
    return dummy.left
"""
