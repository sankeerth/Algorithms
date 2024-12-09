"""
637. Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""
from Tree.python.common.tree_operations import deserialize


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lValues, res = [], []
        
        def dfs(root, level):
            if root:
                if len(lValues) == level:
                    lValues.append([])
                
                lValues[level].append(root.val)
                
                dfs(root.left, level+1)
                dfs(root.right, level+1)

        dfs(root, 0)
        for values in lValues:
            res.append(sum(values)/len(values))

        return res


sol = Solution()
print(sol.averageOfLevels(deserialize('[3,9,20,15,7]')))


"""
My original solution:

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        average = []
        nodes_in_level = []

        def preorder(node, level):
            if node:
                if level >= len(nodes_in_level):
                    nodes_in_level.append(1)
                    average.append(node.val)
                else:
                    nodes_in_level[level] += 1
                    average[level] += node.val
                preorder(node.left, level + 1)
                preorder(node.right, level + 1)

        preorder(root, 0)

        return [(x * 1.0) / y for x, y in zip(average, nodes_in_level)]
"""


"""
leetcode solution in discuss.

def averageOfLevels(self, root):
    info = []
    def dfs(node, depth = 0):
        if node:
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
    dfs(root)

    return [s/float(c) for s, c in info]
"""
