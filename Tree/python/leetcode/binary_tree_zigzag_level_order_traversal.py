"""
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from Tree.python.common.tree_operations import deserialize, TreeNode, print_levelorder_leetcode_style


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, zigzag = [], []

        queue = [(root, 0)]
        while queue:
            root, level = queue.pop(0)
            if len(res) == level:
                res.append([])
            res[level].append(root.val)

            if root.left:
                queue.append((root.left, level+1))
            if root.right:
                queue.append((root.right, level+1))


        for i, l in enumerate(res):
            if i % 2 == 0:
                zigzag.append(l)
            else:
                zigzag.append(l[::-1])

        return zigzag


sol = Solution()
print_levelorder_leetcode_style(sol.pruneTree(deserialize('[3,9,20,null,null,15,7]')))
print_levelorder_leetcode_style(sol.pruneTree(deserialize('[]')))
print_levelorder_leetcode_style(sol.pruneTree(deserialize('[1]')))


"""
DFS solution is easier:

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = defaultdict(deque)
        maxlevel = 0
        zigzag = []

        def dfs(root, level):
            nonlocal maxlevel
            if not root:
                return
            
            maxlevel = max(maxlevel, level)
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, 0)

        for level in range(maxlevel+1):
            zigzag.append(list(res[level]))

        return zigzag
"""
