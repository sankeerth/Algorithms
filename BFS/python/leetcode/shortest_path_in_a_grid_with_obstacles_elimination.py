"""
1293. Shortest Path in a Grid with Obstacles Elimination

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). 
In one step, you can move up, down, left or right from and to an empty cell.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the 
lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. 
If it is not possible to find such walk return -1.

Example 1:
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.

Constraints:
grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue, visited = list(), set()
        rows, cols = len(grid), len(grid[0])

        def neighbors(r, c):
            for x, y in ((r-1,c), (r, c+1), (r+1, c), (r, c-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        def bfs():
            while queue:
                i, j, count, k = queue.pop(0)
                if i == rows-1 and j == cols-1:
                    return count

                for x, y in neighbors(i, j):
                    if grid[x][y] == 0 and (x, y, k) not in visited:
                        visited.add((x, y, k))
                        queue.append((x, y, count+1, k))
                    elif grid[x][y] == 1 and k > 0 and (x, y, k-1) not in visited:
                        visited.add((x, y, k-1))
                        queue.append((x, y, count+1, k-1))
                        
            return -1

        queue.append((0, 0, 0, k))
        visited.add((0, 0, k))
        return bfs()


s = Solution()
print(s.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))
print(s.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1))
print(s.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 2))
print(s.shortestPath([[0]], 1))

"""
check https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/453652/Manhattan-distance-instead-of-normal-goal-check
for optimization trick

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        start = m-1, n-1, k
        queue = [(0, start)]
        seen = {start}
        for steps, (i, j, k) in queue:
            if k >= i + j - 1:
                return steps + i + j
            for i, j in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if m > i >= 0 <= j < n:
                    state = i, j, k - grid[i][j]
                    if state not in seen and state[2] >= 0:
                        queue.append((steps + 1, state))
                        seen.add(state)
        return -1
"""
