"""
1219. Path with Maximum Gold

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
"""
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        if not grid:
            return maxGold

        def getMaximumGoldForPos(i, j):
            if grid[i][j] == 0:
                return 0

            current = grid[i][j]
            grid[i][j] = 0
            up, right, down, left = 0, 0, 0, 0
            
            if i-1 >= 0:
                up = getMaximumGoldForPos(i-1, j)
            if j+1 < len(grid[0]):
                right = getMaximumGoldForPos(i, j+1)
            if i+1 < len(grid):
                down = getMaximumGoldForPos(i+1, j)
            if j-1 >= 0:
                left = getMaximumGoldForPos(i, j-1)

            path = max(up, right, down, left)
            grid[i][j] = current
            
            return current + path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxGoldAtPos = getMaximumGoldForPos(i, j)
                    maxGold = max(maxGold, maxGoldAtPos)

        return maxGold


s = Solution()
print(s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
print(s.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))

"""
Time complexity:

If k cells have gold, each dfs takes O(4^k) time, since we recurse to 4 neighbors.
We run the dfs on k cells, and iterate over m*n cells to find them.
Our total runtime is O((k*4^k) + mn).
"""

"""
Without the optimization - calling the recursive fn to determine the boundary condition

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        if not grid:
            return maxGold

        def getMaximumGoldForPos(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            current = grid[i][j]
            grid[i][j] = 0
            up = getMaximumGoldForPos(i-1, j)
            right = getMaximumGoldForPos(i, j+1)
            down = getMaximumGoldForPos(i+1, j)
            left = getMaximumGoldForPos(i, j-1)

            path = max(up, right, down, left)
            grid[i][j] = current
            
            return current + path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxGoldAtPos = getMaximumGoldForPos(i, j)
                    maxGold = max(maxGold, maxGoldAtPos)

        return maxGold
"""
