"""
1644. Lowest Common Ancestor of a Binary Tree II

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. 
All values of the nodes in the tree are unique.
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants 
(where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
"""
from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def LCA(root):
            nonlocal lca
            if not root:
                return False
            left = LCA(root.left)
            right = LCA(root.right)

            current = root == p or root == q

            if current + left + right >= 2:
                lca = root
            
            return current or left or right
        
        LCA(root)
        return lca


sol = Solution()
r = deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
print_levelorder_leetcode_style(sol.lowestCommonAncestor(r, r.left, r.left.right.right))
print_levelorder_leetcode_style(sol.lowestCommonAncestor(r, r.left.left, r.left.right))
print_levelorder_leetcode_style(sol.lowestCommonAncestor(r, r.left.left.left, None))


"""
Iterative solution using parent:

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue, parent = [root], {root: None}
        ancestors = set()

        while p not in parent or q not in parent:
            if not queue:
                break
            node = queue.pop()
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
            
        if p not in parent or q not in parent:
            return None
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q
"""


"""
My older solution:

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        visited = set()
        
        def lowestCommonAncestorRecursive(root):
            if not root:
                return None

            if root is p or root is q:
                visited.add(root)
                if len(visited) == 2:
                    return root

            left = lowestCommonAncestorRecursive(root.left)
            right = lowestCommonAncestorRecursive(root.right)

            if root is p or root is q:
                return root
            
            if left and right:
                return root

            return left if left else right

        lca = lowestCommonAncestorRecursive(root)
        if len(visited) == 2:
            return lca
        return None
"""
