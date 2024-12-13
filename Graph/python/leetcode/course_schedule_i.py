"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for i,j in prerequisites:
            adjList[i].append(j)
            if not adjList[j]:
                pass

        visited = set()
        
        def isCycle(i, path):
            visited.add(i)
            path.add(i)

            for j in adjList[i]:
                if j in path:
                    return True
                # visited check is imp so don't end up visiting the neighbor that was already visited from another node and no cycle was found (results in TLE)    
                if j not in visited and isCycle(j, path): 
                    return True
            
            path.discard(i)
            return False
        
        for i in adjList:
            if i not in visited:
                if isCycle(i, set()):
                    return False
        
        return True


sol = Solution()
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(2, [[1,0],[0,1]]))
print(sol.canFinish(6, [[1,0],[2,0],[2,1],[4,3],[5,4]]))
print(sol.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))


"""
Solution with Topological Sort Using Kahn's Algorithm (Indegree)

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i,j in prerequisites:
            adjList[j].append(i)
            indegree[i] += 1

        numVisited = 0
        queue = []

        for node, val in enumerate(indegree):
            if val == 0:
                queue.append(node)

        while queue:
            node = queue.pop(0)
            numVisited += 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return numVisited == numCourses
"""
