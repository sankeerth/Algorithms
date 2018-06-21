"""
834. Sum of Distances in Tree

An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
"""
from collections import defaultdict


class Solution(object):
    """
    Explanation:
    When we move our root from one node to its connected node, one part of nodes get closer, one the other part get further.
    If we know exactly hom many nodes in both parts, we can solve this problem.

    With one single traversal in tree, we should get enough information for it and don't need to do it again and again.

    Explanation:
    0. Let's solve it with node 0 as root.

    Initial an array of hashset tree, tree[i] contains all connected nodes to i.
    Initial an array count, count[i] counts all nodes in the subtree i.
    Initial an array of res, res[i] counts sum of distance in subtree i.

    Post order dfs traversal, update count and res:
    count[root] = sum(count[i]) + 1
    res[root] = sum(res[i]) + sum(count[i])

    Pre order dfs traversal, update res:
    When we move our root from parent to its child i, count[i] points get 1 closer to root, n - count[i] nodes get 1
    further to the root.
    res[i] = res[root] - count[i] + N - count[i]

    return res, done.
    """
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = defaultdict(set)
        res = [0] * N
        count = [0] * N

        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    dfs(i, seen)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
            count[root] += 1

        def preorder(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    res[i] = res[root] - count[i] + N - count[i]
                    preorder(i, seen)

        dfs()
        preorder()
        return res


sol = Solution()
print(sol.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
