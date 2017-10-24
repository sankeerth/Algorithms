"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        grid = list()
        for i in range(m):
            grid.append(list([1] * n))

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]


sol = Solution()
print(sol.uniquePaths(1,1))
print(sol.uniquePaths(1,2))
print(sol.uniquePaths(3,5))
print(sol.uniquePaths(7,3))
print(sol.uniquePaths(12,23))
