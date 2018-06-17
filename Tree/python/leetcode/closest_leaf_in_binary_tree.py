"""
742. Closest Leaf in a Binary Tree

Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
"""

from Tree.python.common.tree_operations import deserialize


class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0

        distance_dict = dict()

        def postorder(root):
            if root:
                if not root.left and not root.right:
                    distance_dict[root.val] = (1, root.val)
                    return 1, root.val
                else:
                    left, l_leaf = postorder(root.left)
                    right, r_leaf = postorder(root.right)
                    distance_dict[root.val] = (min(left, right) + 1, l_leaf if left < right else r_leaf)
                    return distance_dict[root.val]
            return float('inf'), None

        postorder(root)

        if root.val == k:
            return distance_dict[k][1]

        result = 0

        def preorder(root, parent=None):
            nonlocal result
            if root:
                if root.val == k:
                    cur_val = distance_dict[root.val]
                    result = distance_dict[parent.val][1] if distance_dict[parent.val][0] < cur_val[0] else cur_val[1]
                else:
                    preorder(root.left, root)
                    preorder(root.right, root)

        preorder(root)
        return result


sol = Solution()
print(sol.findClosestLeaf(deserialize("[1, 3, 2]"), 1))
print(sol.findClosestLeaf(deserialize("[1]"), 1))
print(sol.findClosestLeaf(deserialize("[1,2,3,4,null,null,null,5,null,6]"), 2))
print(sol.findClosestLeaf(deserialize("[1,2,3,4,null,null,null,5,null,6]"), 4))
