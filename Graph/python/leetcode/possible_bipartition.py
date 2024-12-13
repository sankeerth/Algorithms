"""
886. Possible Bipartition

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, 
return true if it is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= ai < bi <= n
All the pairs of dislikes are unique.
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        group = [-1] * (n+1)

        # need to convert to undirected graph, else one test with lots of dislikes fails (haven't figured out why undirected graph is needed and directed graph isn't sufficient)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        
        def isBipartite(i, g):
            group[i] = g
            for j in graph[i]:
                if group[i] == group[j]:
                    return False
                if group[j] == -1:
                    if not isBipartite(j, 1-g):
                        return False
            return True

        for i in range(1, n+1):
            if group[i] == -1:
                if not isBipartite(i, 0):
                    return False
        
        return True


sol = Solution()
print(sol.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
print(sol.possibleBipartition(3, [[1,2],[1,3],[2,3]]))


"""
BFS solution:

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        group = [-1] * (n+1)

        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        
        def isBipartite(i):
            queue = [i]
            group[i] = 0
            
            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if group[v] == group[u]:
                        return False
                    if group[v] == -1:
                        group[v] = 1-group[u]
                        queue.append(v)
            return True

        for i in range(1, n+1):
            if group[i] == -1:
                if not isBipartite(i):
                    return False
        
        return True
"""
