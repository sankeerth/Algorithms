"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a 
network where connections[i] = [a, b] represents a connection between servers a and b. Any server can 
reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:
1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""
from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        result = []
        reachableNodes = defaultdict(set)

        for connection in connections:
            src, dest = connection
            reachableNodes[src].add(dest)
            reachableNodes[dest].add(src)

        def reachable(src, dest, visited):
            if dest in reachableNodes[src]:
                return True

            visited.add(src)
            for node in reachableNodes[src]:
                if node not in visited and reachable(node, dest, visited):
                    reachableNodes[src].add(dest)
                    return True

            return False

        for edge in connections:
            src, dest = edge
            reachableNodes[src].remove(dest)
            reachableNodes[dest].remove(src)

            visited = set()
            visited.add(src)
            isReachable = True

            if len(reachableNodes[src]) == 0 or len(reachableNodes[dest]) == 0:
                isReachable = False
            else:
                for node in reachableNodes[src]:
                    if node not in visited:
                        isReachable = reachable(node, dest, visited)
                        if isReachable:
                            break

            if not isReachable:        
                result.append([src, dest])

            reachableNodes[src].add(dest)
            reachableNodes[dest].add(src)

        return result


s = Solution()
print(s.criticalConnections(4, [[0,1],[1,2],[2,3],[3,0]]))
print(s.criticalConnections(3, [[0,1],[1,2],[2,0]]))
print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
print(s.criticalConnections(6, [[0,1],[1,2],[2,3],[3,4],[4,5]]))
print(s.criticalConnections(6, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]]))
print(s.criticalConnections(7, [[0,1],[1,2],[2,3],[3,1],[0,4],[4,5],[5,0]]))
