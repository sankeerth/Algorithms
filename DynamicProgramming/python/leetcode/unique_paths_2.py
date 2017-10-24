"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0

        grid = list()
        for i in range(m):
            grid.append(list([1] * n))

        grid[0][0] = 0 if obstacleGrid[0][0] else 1

        for i in range(1, m):
            if grid[i - 1][0] and not obstacleGrid[i][0]:
                grid[i][0] = 1
            else:
                grid[i][0] = 0

        for i in range(1, n):
            if grid[0][i - 1] and not obstacleGrid[0][i]:
                grid[0][i] = 1
            else:
                grid[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]


sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstacles([[1,0,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstacles([[0,1,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstacles([[0,0,1],[0,0,0],[0,0,0]]))
