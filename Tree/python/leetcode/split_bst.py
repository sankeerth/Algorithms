"""
776. Split BST

Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where the first subtree has nodes that are all smaller or equal 
to the target value, while the second subtree has all nodes that are greater than the target value. It is not necessarily the case that the tree contains a node with the value target.
Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, 
if they are both in the same subtree after the split, then node c should still have the parent p.
Return an array of the two roots of the two subtrees in order.

Example 1:
Input: root = [4,2,6,1,3,5,7], target = 2
Output: [[2,1],[4,3,6,null,null,5,7]]

Example 2:
Input: root = [1], target = 1
Output: [[1],[]]

Constraints:
The number of nodes in the tree is in the range [1, 50].
0 <= Node.val, target <= 1000
"""


# Editorial solution (recursive)
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def split(root):
            # Base case: if root is None, return two None values
            if not root:
                return [None, None]
            # If root's value is greater than target,
            # recursively split left subtree
            if root.val > target:
                left = split(root.left)
                # Attach the right part of the split to root's left subtree
                root.left = left[1]
                return [left[0], root]
            else: # Otherwise, recursively split right subtree
                right = split(root.right)
                # Attach the left part of the split to root's right subtree
                root.right = right[0]
                return [root, right[1]]

        return split(root)


"""
Editorial solution (iterative)


class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:

        # List to store the two split trees
        ans = [None, None]

        # If root is None, return the empty list
        if not root:
            return ans
        # Stack to traverse the tree and find the split point
        stack = []
        # Find the node with the value closest to the target
        while root:
            stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        # Process nodes in reverse order from the stack to perform the split
        while stack:
            curr = stack.pop()
            if curr.val > target:
                # Assign current node's left child to the subtree
                # containing nodes greater than the target
                curr.left = ans[1]
                # current node becomes the new root of this subtree
                ans[1] = curr
            else:
                # Assign current node's right child to the subtree
                # containing nodes smaller than the target
                curr.right = ans[0]
                # current node becomes the new root of this subtree
                ans[0] = curr
        return ans
"""
