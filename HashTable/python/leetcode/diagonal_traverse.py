"""
498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        res = []

        for i in range(rows):
            for j in range(cols):
                diagonals[i+j].append(mat[i][j])

        for d in range(rows+cols-1):
            if d % 2 == 0:
                res += diagonals[d][::-1]
            else:
                res += diagonals[d]

        return res


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,4,7,5,3,6,8,9]
print(sol.findDiagonalOrder([[1,2],[3,4]])) # [1,2,3,4]
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])) # [1,2,4,7,5,3,6,8,10,13,11,9,12,14,15]
