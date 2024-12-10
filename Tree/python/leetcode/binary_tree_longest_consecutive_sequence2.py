"""
549. Binary Tree Longest Consecutive Sequence II

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
"""
from Tree.python.common.tree_operations import deserialize


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if not root:
            return result

        def postorder(root, prev):
            nonlocal result
            if not root:
                return 0

            left = postorder(root.left, root.val)
            right = postorder(root.right, root.val)

            l_c, r_c = 1, 1
            if root.left and (root.left.val == root.val + 1 or root.left.val == root.val - 1):
                l_c = max(l_c, left + 1)
            if root.right and (root.right.val == root.val + 1 or root.right.val == root.val - 1):
                r_c = max(r_c, right + 1)
            if root.left and root.right:
                if (root.val == root.left.val+1 and root.val == root.right.val-1) or (root.val == root.left.val-1 and root.val == root.right.val+1):
                    result = max(result, left + right + 1)
            result = max(result, max(l_c, r_c))

            if root.val == prev + 1:
                if root.left and root.left.val == root.val + 1 and root.right and root.right.val == root.val + 1:
                    return max(l_c, r_c)
                elif root.left and root.left.val == root.val + 1:
                    return l_c
                elif root.right and root.right.val == root.val + 1:
                    return r_c

            if root.val == prev - 1:
                if root.left and root.left.val == root.val - 1 and root.right and root.right.val == root.val - 1:
                    return max(l_c, r_c)
                elif root.left and root.left.val == root.val - 1:
                    return l_c
                elif root.right and root.right.val == root.val - 1:
                    return r_c

            return 1

        postorder(root, float('inf'))

        return result


sol = Solution()
print(sol.longestConsecutive(deserialize("[1,null,3,2,4,null,null,null,5]")))
print(sol.longestConsecutive(deserialize("[2,3,3,4,null,null,4,5,null,3,5,null,null,null,2,null,6,1]")))
print(sol.longestConsecutive(deserialize("[2,null,3,2,null,1]")))
print(sol.longestConsecutive(deserialize("[1,null,2,3,3,null,4,null,4,null,null,5]")))
print(sol.longestConsecutive(deserialize("[1,null,2,3,4,null,4,null,5,null,null,6,null,7,7,null,8,8,null,null,null,null,9]")))
print(sol.longestConsecutive(deserialize("[4,3,3,4,null,null,4,5,null,3,5,null,null,null,null,null,6]")))
print(sol.longestConsecutive(deserialize("[2,3,3,4,null,null,4,5,null,3,5,null,null,null,null,null,6]")))


"""
leetcode discuss solution: # much simpler!

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postorder(root, parent):
            nonlocal res
            if not root:
                return 0, 0
            
            leftInc, leftDec = postorder(root.left, root)
            rightInc, rightDec = postorder(root.right, root)

            res = max(res, leftInc+rightDec+1, leftDec+rightInc+1)
            
            if root.val == parent.val-1: # decreasing
                return 0, max(leftDec, rightDec)+1
            if root.val == parent.val+1: # increasing
                return max(leftInc, rightInc)+1, 0
            
            return 0,0
            
        postorder(root, root)
        return res 
"""
