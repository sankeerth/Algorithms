"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        res = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])

        return res ** 2


sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(sol.maximalSquare([["1","0","1","0","0","1","1","1","0"],["1","1","1","0","0","0","0","0","1"],["0","0","1","1","0","0","0","1","1"],["0","1","1","0","0","1","0","0","1"],["1","1","0","1","1","0","0","1","0"],["0","1","1","1","1","1","1","0","1"],["1","0","1","1","1","0","0","1","0"],["1","1","1","0","1","0","0","0","1"],["0","1","1","1","1","0","0","1","0"],["1","0","0","1","1","1","0","0","0"]]))


"""
Leetcode solution: O(N) space

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols+1)
        res, prevDiag = 0, 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(prevDiag, dp[j-1], dp[j]) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                prevDiag = temp
        
        return res ** 2
"""

"""
My solution that fails to consider area of smaller squares:

#     0   1   2   3   4   5   6   7   8 
# 0 ["1","0","1","0","0","1","1","1","0"],
# 1 ["1","1","1","0","0","0","0","0","1"],
# 2 ["0","0","1","1","0","0","0","1","1"],
# 3 ["0","1","1","0","0","1","0","0","1"],
# 4 ["1","1","0","1","1","0","0","1","0"],
# 5 ["0","1","1","1","1","1","1","0","1"],
# 6 ["1","0","1","1","1","0","0","1","0"],
# 7 ["1","1","1","0","1","0","0","0","1"],
# 8 ["0","1","1","1","1","0","0","1","0"],
# 9 ["1","0","0","1","1","1","0","0","0"]

Output: 9 | Expected: 4
Result 9 at (i, j) -> (6, 4)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[[0, 0]] * cols for _ in range(rows)]
        res = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    left = 1 if j == 0 else dp[i][j-1][0] + 1
                    up = 1 if i == 0 else dp[i-1][j][1] + 1
                    dp[i][j] = [left, up]

                    minOfLeftAndUp = min(left, up)
                    minOfLeftDiag = 0 if i == 0 or j == 0 else min(dp[i-1][j-1][0], dp[i-1][j-1][1])
                    if minOfLeftAndUp - 1 == minOfLeftDiag:
                        res = max(res, minOfLeftAndUp * minOfLeftAndUp)

        return res
"""
