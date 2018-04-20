"""
508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""

from Tree.python.common.tree_operations import deserialize
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        subtree_sum = defaultdict(int)

        if not root:
            return []

        def postorder(root):
            if not root:
                return 0
            else:
                left = postorder(root.left)
                right = postorder(root.right)
                val = root.val + left + right
                subtree_sum[val] += 1
                return val

        postorder(root)
        max_val = max(subtree_sum.items(), key=lambda v: v[1])
        result = list()
        for key, val in subtree_sum.items():
            if val == max_val[1]:
                result.append(key)

        return result


sol = Solution()
print(sol.findFrequentTreeSum(deserialize('[5,2,-5]')))
print(sol.findFrequentTreeSum(deserialize('[5,2,-3]')))
