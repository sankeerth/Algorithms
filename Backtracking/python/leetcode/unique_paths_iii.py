"""
980. Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:
1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:
1 <= grid.length * grid[0].length <= 20
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        zeros, start = 0, (0, 0)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    zeros += 1

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] != -1:
                    yield x, y

        def dfs(i, j, zeros):
            if zeros == 0 and grid[i][j] == 2:
                return 1
            
            val = grid[i][j]
            grid[i][j] = -1

            res = 0
            for x, y in neighbors(i, j):
                res += dfs(x, y, zeros-1)

            grid[i][j] = val
            return res

        return dfs(start[0], start[1], zeros+1) # zeros+1 to account for 1 which is the start


s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(s.uniquePathsIII([[1,0,0],[0,0,0],[0,0,2]]))
print(s.uniquePathsIII([[0,1],[2,0]]))
print(s.uniquePathsIII([[1,0,0],[0,0,0],[0,0,2],[0,0,0],[0,0,0]]))
print(s.uniquePathsIII([[0,0,0],[0,0,0],[0,0,2],[0,0,0],[0,0,1]]))
print(s.uniquePathsIII([[1]]))
