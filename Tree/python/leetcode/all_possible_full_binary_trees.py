"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Return a list of all possible full binary trees with N nodes. 
Each element of the answer is the root node of one possible tree.
Each node of each tree in the answer must have node.val = 0. You may return the final list of trees in any order.

Example 1:
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

Note:
1 <= N <= 20
"""
from typing import List
from Tree.python.common.tree_operations import print_trees


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []

        memoizedFBTs = {}
        memoizedFBTs[1] = [TreeNode(0)]

        def allPossibleFBTRecursive(N):
            if N in memoizedFBTs:
                return memoizedFBTs[N]

            nodes = []
            for i in range(2, N, 2):
                left = allPossibleFBTRecursive(i-1)
                right = allPossibleFBTRecursive(N-i)
                
                for lNode in left:
                    for rNode in right:
                        node = TreeNode(0)
                        node.left = lNode
                        node.right = rNode
                        nodes.append(node)
            
            memoizedFBTs[N] = nodes
            return nodes

        return allPossibleFBTRecursive(N)


s = Solution()
print_trees(s.allPossibleFBT(7))


"""
My solution without memoization or dp

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []

        def allPossibleFBTRecursive(N):
            nodes = []
            if N == 1:
                return [TreeNode(0)]
            for i in range(2, N, 2):
                left = allPossibleFBTRecursive(i-1)
                right = allPossibleFBTRecursive(N-i)
                
                for lNode in left:
                    for rNode in right:
                        node = TreeNode(0)
                        node.left = lNode
                        node.right = rNode
                        nodes.append(node)
            
            return nodes

        return allPossibleFBTRecursive(N)
"""
