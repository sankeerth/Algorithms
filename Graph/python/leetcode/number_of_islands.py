"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        array = [i for i in range(m * n)]
        size = [1 for _ in range(m * n)]
        x_coor = [-1, 0]
        y_coor = [0, -1]

        def root(x):
            while x != array[x]:
                x = array[x]
            return x

        def union(x, y):
            root_x = root(x)
            root_y = root(y)

            if root_x == root_y:
                return False

            if size[root_x] < size[root_y]:
                size[root_y] += size[root_x]
                array[root_x] = root_y
            else:
                size[root_x] += size[root_y]
                array[root_y] = root_x

            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    for k in range(len(x_coor)):
                        x, y = i + x_coor[k], j + y_coor[k]
                        if -1 < x < m and -1 < y < n and grid[x][y] == "1":
                            if union(i * n + j, x * n + y):
                                    result -= 1
        return result


sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(sol.numIslands([["1", "0", "1"]]))
print(sol.numIslands([["0", "1"], ["1", "1"]]))
print(sol.numIslands([[]]))


"""
My DFS and BFS solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def neighbors(i, j):
            for x, y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        def dfs(i, j):
            visited.add((i,j))
            for x, y in neighbors(i, j):
                if grid[x][y] == "1" and (x,y) not in visited:
                    dfs(x, y)

        def bfs(i, j):
            queue = [(i,j)]
            visited.add((i,j))
            while queue:
                i, j = queue.pop(0)
                for x, y in neighbors(i, j):
                    if grid[x][y] == "1" and (x,y) not in visited:
                        queue.append((x,y))
                        visited.add((x,y)) # imp to avoid TLE else duplicate neighbors will be added to the queue


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    bfs(i, j)
        
        return res
"""
