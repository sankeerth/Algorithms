"""
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1, and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit 
from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Example 3:
Input: graph = [[1],[]]
Output: [[0,1]]

Example 4:
Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]

Example 5:
Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]

Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
"""
from typing import List
from collections import defaultdict


# DFS with memoization
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        dp = defaultdict(list)
        target = len(graph)-1

        def dfs(src, path):
            if src == target:
                result.append(path)
                return [[target]]

            for dest in graph[src]:
                if dp[dest]:
                    for p in dp[dest]:
                        result.append(path + p)
                        dp[src].append([src] + p)
                    continue

                res = dfs(dest, path + [dest])
                for p in res:
                    dp[src].append([src] + p)
            
            return dp[src]

        dfs(0, [0])
        return result


s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
print(s.allPathsSourceTarget([[1],[]]))
print(s.allPathsSourceTarget([[1,2,3],[2],[3],[]]))
print(s.allPathsSourceTarget([[1,3],[2],[3],[]]))
print(s.allPathsSourceTarget([[1,2,3],[4],[1,4],[2],[]]))


"""
BFS solution

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result, queue = [], []

        queue.append((0, [0]))
        while queue:
            src, path = queue.pop()
            for dest in graph[src]:
                if dest == len(graph)-1:
                    result.append(path + [dest])
                else:
                    queue.append((dest, path + [dest]))

        return result
"""

"""
DFS without memoization

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        def dfs(src, path):
            for dest in graph[src]:
                if dest == len(graph)-1:
                    result.append(path + [dest])
                    continue
                dfs(dest, path + [dest])

        dfs(0, [0])
        return result
"""

"""
Backtracking solution with out memoization

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []

        def dfs(src):
            path.append(src)
            if src == len(graph)-1:
                result.append(list(path))
            else:
                for dest in graph[src]:
                    dfs(dest)
            path.pop()

        dfs(0)
        return result
"""

"""
Complexity of Backtracking solution:

Let N be the number of nodes in the graph.
First of all, let us estimate how many paths there are at maximum to travel from the Node 0 to the 
Node N-1 for a graph with NN nodes.

Let us start from a graph with only two nodes. As one can imagine, there is only one single path 
to connect the only two nodes in the graph.

Now, let us add a new node into the previous two-nodes graph, we now have two paths, one from the previous path, 
the other one is bridged by the newly-added node.

If we continue to add nodes to the graph, one insight is that every time we add a new node into the graph, 
the number of paths would double.

With the newly-added node, new paths could be created by preceding all previous paths with the newly-added node.

As a result, for a graph with NN nodes, at maximum, there could be ∑ {i=0}^{N-2}{2^i} = 2^{N-1} - 1
number of paths between the starting and the ending nodes.

Time Complexity: O(2^N ⋅ N)

As we calculate shortly before, there could be at most 2^{N-1} - 1 possible paths in the graph.
For each path, there could be at most N-2N−2 intermediate nodes, i.e. it takes O(N) time to build a path.
To sum up, a loose upper-bound on the time complexity of the algorithm would be (2^{N-1} - 1). O(N), 
where we consider it takes O(N) efforts to build each path.

It is a loose uppper bound, since we could have overlapping among the paths, therefore the efforts to build certain paths could benefit others.

Space Complexity: O(2^N⋅N)

Similarly, since at most we could have 2^{N-1}-1 paths as the results and each path can contain up to N nodes, 
the space we need to store the results would be O(2^N ⋅N).

Since we also applied recursion in the algorithm, the recursion could incur additional memory consumption in the function call stack. 
The stack can grow up to N consecutive calls. Meanwhile, along with the recursive call, we also keep the state of the current path, 
which could take another O(N) space. Therefore, in total, the recursion would require additional O(N) space.

To sum up, the space complexity of the algorithm is O(2^N ⋅ N) + O(N) = O(2^N ⋅ N).
"""

"""
Complexity of DP solution:

Same as Backtracking solution since the paths need to be copied over (appended) to store the new path 
which is the same as visiting the node once without memo.

The two approach might have the same asymptotic time complexity. However, in practice the DP approach is 
slower than the backtracking approach, since we copy the intermediate paths over and over.
"""
