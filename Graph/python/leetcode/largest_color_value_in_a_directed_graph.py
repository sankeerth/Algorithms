"""
1857. Largest Color Value in a Directed Graph

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). 
You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. 
The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:
Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.

Constraints:
n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
"""


"""
Leetcode discuss solution:

Let dp[i][j] be the maximum frequency of jth letter till we have reached ith node.
The value of i is from 0 to n-1 and j is from 0 to 25.(a to z)
When we visit ith node, we should consider all the paths that lead to the ith node for calculating maximum frequency.

We maintain a list degree, which denotes the indegree of the current node.
Initially we push all the nodes which have degree = 0 in the queue.
Let count represent the number of nodes that have been popped.

We do the following till queue is empty or till count becomes n:

Pop node from queue. Increment the count.
Increment dp[node][color[node]] by 1.
Iterate through all the neighbours of currnode.
a. Iterate through all the characters.
b. Update dp[neighbour][char] = max(dp[neighbour][char], dp[node][char])
Decrease degree of the neighbour by 1. If the degree of the neighbour becomes 0, push it in the queue.
After count becomes n and if the queue is not empty, that means there is a cycle in the graph. Return -1 in this case.
Else return max from dp.


def largestPathValue(self, color: str, edges: List[List[int]]) -> int:
        n = len(color)
        graph = [[] for node in range(n)]
        deg = [0 for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            deg[v] += 1
        q = []
        dp = [[0 for j in range(26)]for i in range(n)]
        for i in range(n):
            if deg[i] == 0:
                q.append(i)
        count = 0
        ans = -1
        while q != []:
            currnode = q.pop(0)
            count += 1
            dp[currnode][ord(color[currnode])-ord('a')] += 1
            ans = max(ans, dp[currnode][ord(color[currnode])-ord('a')])
            for neigh in graph[currnode]:
                for i in range(26):
                    dp[neigh][i] = max(dp[neigh][i], dp[currnode][i])
                deg[neigh] -= 1
                if deg[neigh] == 0:
                    q.append(neigh)
            if count == n:
                break
        
        if q != [] or count < n:
            return -1
        return ans
"""
