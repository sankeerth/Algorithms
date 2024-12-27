"""
Given a binary tree, return the vertical order traversal of its nodes' values. 
(ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodesInCol = defaultdict(list)
        queue = [(root, 0)]
        minCol, maxCol = float('inf'), float('-inf')
        res = []
        
        while queue:
            root, col = queue.pop(0)
            nodesInCol[col].append(root.val)
            
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if root.left:
                queue.append((root.left, col-1))
            if root.right:
                queue.append((root.right, col+1))

        for col in range(minCol, maxCol+1):
            res.append(nodesInCol[col])

        return res


s = Solution()
print(s.verticalOrder(deserialize('[3,9,8,4,0,1,7]')))
print(s.verticalOrder(deserialize('[3,9,20,null,null,15,7]')))
print(s.verticalOrder(deserialize('[3,9,8,4,0,1,7,null,11,null,2,5]')))

"""
DFS approach:

Do all the nodes first with root as 0 and left is root-1 and right is root+1.
Get the min (left most) and start again with root as abs(min) and add the nodes to the
respective index in the result

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vLevels = defaultdict(list)
        res = []

        def dfs(root, ver, hor): # Need horizontal level here to ensure nodes are added from top to bottom
            if root:
                vLevels[ver].append((root.val, hor))
                dfs(root.left, ver-1, hor+1)
                dfs(root.right, ver+1, hor+1)

        dfs(root, 0, 0)
        maxLevel, minLevel = float('-inf'), float('inf')
        for level in vLevels:
            vLevels[level].sort(key=lambda x : x[1]) # TT for sorting req: [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
            maxLevel = max(maxLevel, level)
            minLevel = min(minLevel, level)

        for level in range(minLevel, maxLevel+1):
            nodes = []
            for node, _ in vLevels[level]:
                nodes.append(node)
            res.append(nodes)

        return res
"""
