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
        lefts, rights = [], []
        rights.append([])

        def verticalOrderRecursive(root, col, isLeft):
            if root:
                if isLeft:
                    lefts.append([])
                else:
                    rights.append([])

                verticalOrderRecursive(root.left, col-1, True)
                if col <= 0:
                    lefts[abs(col)].append(root.val)
                else:
                    rights[col].append(root.val)
                verticalOrderRecursive(root.right, col+1, False)

        verticalOrderRecursive(root, 0, True)
        return lefts[::-1] + rights


s = Solution()
# print(s.verticalOrder(deserialize('[3,9,8,4,0,1,7]')))
# print(s.verticalOrder(deserialize('[3,9,20,null,null,15,7]')))
print(s.verticalOrder(deserialize('[3,9,8,4,0,1,7,null,11,null,2,5]')))

"""
Another approach:

Do all the nodes first with root as 0 and left is root-1 and right is root+1.
Get the min (left most) and start again with root as abs(min) and add the nodes to the
respective index in the result
"""