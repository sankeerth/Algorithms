"""
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = 0
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def neighbors(i, j):
            for x, y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            count = 1
            for x, y in neighbors(i, j):
                if matrix[x][y] > matrix[i][j]:
                    count = max(count, dfs(x, y)+1)
            memo[i][j] = count
            return count

        for i in range(rows):
            for j in range(cols):
                if not memo[i][j]:
                    longest = max(longest, dfs(i, j))
        
        return longest


sol = Solution()
print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(sol.longestIncreasingPath([[1]]))
