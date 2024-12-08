"""
742. Closest Leaf in a Binary Tree

Given the root of a binary tree where every node has a unique value and a target integer k, return the value of the nearest leaf node to the target k in the tree.

Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

Example 1:
Input: root = [1,3,2], k = 1
Output: 2
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:
Input: root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.

Example 3:
Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
1 <= Node.val <= 1000
All the values of the tree are unique.
There exist some node in the tree where Node.val == k.
"""
from Tree.python.common.tree_operations import deserialize


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        distances = {}
        
        def findClosestLeafBottomUp(root):
            if not root:
                return float('inf'), None
            if root.left is None and root.right is None:
                distances[root.val] = (1, root.val)
                return 1, root.val
        
            leftDepth, leftLeaf = findClosestLeafBottomUp(root.left)
            rightDepth, rightLeaf = findClosestLeafBottomUp(root.right)

            depth, closestLeaf = min(leftDepth, rightDepth) + 1, 0
            if leftDepth <= rightDepth:
                closestLeaf = leftLeaf
            else:
                closestLeaf = rightLeaf
            
            distances[root.val] = (depth, closestLeaf)
            return depth, closestLeaf

        def findClosestLeafTopDown(root, depth, closestLeafToParent):
            if not root:
                return
            
            if depth+1 < distances[root.val][0]:
                distances[root.val] = (depth+1, closestLeafToParent)
            
            findClosestLeafTopDown(root.left, distances[root.val][0], distances[root.val][1])
            findClosestLeafTopDown(root.right, distances[root.val][0], distances[root.val][1])
        
        findClosestLeafBottomUp(root)
        findClosestLeafTopDown(root, float('inf'), None)

        return distances[k][1]


sol = Solution()
print(sol.findClosestLeaf(deserialize('[1,3,2]')))
print(sol.findClosestLeaf(deserialize('[1]')))
print(sol.findClosestLeaf(deserialize('[1,2,3,4,null,null,null,5,null,6]')))
print(sol.findClosestLeaf(deserialize('[1,2,3,null,null,4,5,6,null,null,7,8,9,10]')))
print(sol.findClosestLeaf(deserialize('[1,3,2,7,4,null,null,null,8,null,5,null,9,null,6,null,10,null,null,null,11]')))


"""
Convert tree to graph using DFS and use BFS to find the closest leaf

from collections import defaultdict

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)

        def dfs(root, parent=None):
            if root:
                graph[root.val].append(parent) # root needs to have None as parent to cover the case [1,2], else both 1 and 2 will be considered as leaf nodes
                if parent:
                    graph[parent].append(root.val)
                dfs(root.left, root.val)
                dfs(root.right, root.val)
        
        dfs(root)
        print(graph)
        queue = [k]
        visited = set([None]) # add None so it is not added to the queue by root node

        while queue:
            node = queue.pop(0)
            visited.add(node)
            if len(graph[node]) <= 1: # covers the case with root the only node
                return node
            
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        
        return -1
"""
