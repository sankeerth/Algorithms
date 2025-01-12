"""
694. Number of Distinct Islands

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
Return the number of distinct islands.

Example 1:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited, distinct = set(), set()
        
        def neighbors(i, j):
            for x, y in [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and (x, y) not in visited:
                    yield x, y

        def bfs(ox, oy, islands):
            queue = [(ox, oy)]
            while queue:
                i, j = queue.pop(0)
                for x, y in neighbors(i, j):
                    islands.append((x-ox, y-oy))
                    visited.add((x, y))
                    queue.append((x, y))
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    islands = [(0, 0)]
                    bfs(i, j, islands)
                    tupIslands = tuple(islands)
                    if tupIslands not in distinct:
                        res += 1
                    distinct.add(tupIslands)
        
        return res


sol = Solution()
print(sol.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(sol.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))

