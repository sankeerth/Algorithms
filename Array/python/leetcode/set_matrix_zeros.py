"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""


class Solution:
    """
    Store the presence of a 0 in first element of the row and first element of the column.
    Ex: 0 in 2nd row will have matrix[2][0] and matrix[0][2] as '0'.
    However, a conflict results in storing the presence of 0 for first row and first column, therefore have a
    variable for storing the value of the column.
    """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if col0 == 0:
                matrix[i][0] = 0

        print(matrix)


sol = Solution()
sol.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
sol.setZeroes([[1, 1, 2, 0], [3, 4, 0, 2], [1, 3, 1, 5]])
sol.setZeroes([[1, 1, 2, 0], [3, 4, 0, 2], [1, 0, 1, 5]])
