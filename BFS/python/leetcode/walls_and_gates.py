"""
286. Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume 
that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
Output:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]

Example 3:
Input: rooms = [[2147483647]]
Output: [[2147483647]]

Example 4:
Input: rooms = [[0]]
Output: [[0]]

Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1
"""
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        queue, visited = list(), set()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        
        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols and rooms[x][y] > 0:
                    yield x, y

        while queue:
            i, j, l = queue.pop(0)
            rooms[i][j] = l

            for x, y in neighbors(i, j):
                if (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y, l+1))

        return rooms


sol = Solution()
print(sol.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))


"""
leetcode comment: I suggest that for this kind of problem using BFS instead of DFS which may lead you to a fail in the 
real interview. DFS may do a lot of duplicate operations.

DFS solution that gives TLE:

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        visited = set()

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y
        
        def dfs(i, j, dist):
            for x, y in neighbors(i, j):
                if rooms[x][y] > 0 and (x, y) not in visited:
                    visited.add((x, y))
                    rooms[x][y] = min(rooms[x][y], dist)
                    dfs(x, y, dist+1)
                    visited.discard((x, y))

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    dfs(i, j, 1)

        return rooms
"""
