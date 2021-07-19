"""
652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:
The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""
from typing import List
from common.tree_operations import TreeNode, deserialize


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        hashMap = {}
        
        def findDuplicateSubtreesRecursive(root):
            if not root:
                return 'N'
            
            left = findDuplicateSubtreesRecursive(root.left)
            right = findDuplicateSubtreesRecursive(root.right)
            string = "{},{},{}".format(str(root.val), left, right)
            
            if string in hashMap:
                if not hashMap[string]:
                    hashMap[string] = True
                    res.append(root)
            else:
                hashMap[string] = False
    
            return string
    
        findDuplicateSubtreesRecursive(root)
        return res


sol = Solution()
print(sol.findDuplicateSubtrees(deserialize('[1,2,3,4,null,2,4,null,null,4]')))
print(sol.findDuplicateSubtrees(deserialize('[2,1,1]')))
print(sol.findDuplicateSubtrees(deserialize('[2,2,2,3,null,3,null]')))
