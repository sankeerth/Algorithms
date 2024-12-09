"""
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]

Constraints:
1 <= n <= 20
"""
from typing import List
from Tree.python.common.tree_operations import print_trees


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        memoized = {1: [TreeNode(0)]}

        def allPossibleFBTRec(n):
            if n in memoized:
                return memoized[n]
            
            nodes = []
            for i in range(2, n, 2):
                left = allPossibleFBTRec(i-1)
                right = allPossibleFBTRec(n-i)
            
                for lNode in left:
                    for rNode in right:
                        node = TreeNode(0)
                        node.left = lNode
                        node.right = rNode
                        nodes.append(node)
            
            memoized[n] = nodes
            return nodes
        
        return allPossibleFBTRec(n)


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
