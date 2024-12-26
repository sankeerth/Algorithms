"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""
from typing import List


class Solution:
    """
    Explanation:
    We start search the matrix from top right corner, initialize the current position to top right corner,
    if the target is greater than the value in current position, then the target can not be in entire row of current
    position because the row is sorted, if the target is less than the value in current position,
    then the target can not in the entire column because the column is sorted too. We can rule out one row or one
    column each time, so the time complexity is O(m+n).
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols-1

        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        
        return False


sol = Solution()
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(sol.searchMatrix([[1,4,7,11,15]], 20))
print(sol.searchMatrix([[1,4,7,11,15]], 4))
print(sol.searchMatrix([[1,4,7],[11,15,19]], 12))
print(sol.searchMatrix([[1,4,7],[11,15,19]], 11))
print(sol.searchMatrix([[1,4,7],[11,15,19]], 19))
