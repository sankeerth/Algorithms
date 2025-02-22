"""
317. Shortest Distance from All Buildings

You are given an m x n grid grid of values 0, 1, or 2, where:
each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.
The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
"""
from typing import List
from collections import defaultdict


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        buildings = {}
        queue, visited = list(), set()

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y
        
        id = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j, 0, id))
                    id += 1
        count = id

        while queue:
            i, j, d, id = queue.pop(0)
            if grid[i][j] == 0:
                if (i, j) not in buildings:
                    buildings[(i, j)] = [0, 0]
                buildings[(i, j)][0] += d
                buildings[(i, j)][1] += 1
            
            for x, y in neighbors(i, j):
                if grid[x][y] == 0 and (x, y, id) not in visited:
                    visited.add((x, y, id))
                    queue.append((x, y, d+1, id))

        res = float('inf')
        for dist, ids in buildings.values():
            if ids == count:
                res = min(res, dist)
        return res if res != float('inf') else -1


sol = Solution()
print(sol.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
print(sol.shortestDistance([[1,0]]))
print(sol.shortestDistance([[1]]))
# failed testcases
print(sol.shortestDistance([[0,2,1],[1,0,2],[0,1,0]]))
print(sol.shortestDistance([[0,2,1],[1,0,0],[0,1,0]]))


"""
My solution above gives TLE in python although the logic and approach is correct.
Leetcode discuss solution:

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = math.inf
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for d in dirs:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == -curr_count:
                        total_sum[next_row][next_col] += curr_step + 1
                        min_distance = min(min_distance, total_sum[next_row][next_col])
                        grid[next_row][next_col] -= 1
                        queue.append([next_row, next_col, curr_step + 1])
            return min_distance
                
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == math.inf:
                        return -1
        
        return min_distance
"""
