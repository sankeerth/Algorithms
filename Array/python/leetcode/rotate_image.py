"""
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, len(matrix)-1
        n = len(matrix)-1

        while i < j:
            for k in range(i, j):
                temp = matrix[k][n-i]
                matrix[k][n-i] = matrix[i][k]
                matrix[i][k] = matrix[n-k][i]
                matrix[n-k][i] = matrix[n-i][n-k]
                matrix[n-i][n-k] = temp

            i += 1
            j -= 1

        for row in matrix:
            print(row)


sol = Solution()
sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sol.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])

"""
Above solution worked out as:

for a 4*4 matrix
n = 3

i=0, k=0        i=0, k=1        i=0, k=2        i=1, k=1
0,0 -> 0,3      0,1 -> 1,3      0,2 -> 2,3      1,1 -> 1,2
0,3 -> 3,3      1,3 -> 3,2      2,3 -> 3,1      1,2 -> 2,2
3,3 -> 3,0      3,2 -> 2,0      3,1 -> 1,0      2,2 -> 2,1
3,0 -> 0,0      2,0 -> 0,1      1,0 -> 0,2      2,1 -> 1,1
"""


"""
Leetcode discuss solution:

/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}
"""


"""
Leetcode discuss solution:

The idea was firstly transpose the matrix and then flip it symmetrically. For instance,
1  2  3             
4  5  6
7  8  9

after transpose, it will be swap(matrix[i][j], matrix[j][i])
1  4  7
2  5  8
3  6  9

Then flip the matrix horizontally. (swap(matrix[i][j], matrix[i][matrix.length-1-j])
7  4  1
8  5  2
9  6  3

public class Solution {
    public void rotate(int[][] matrix) {
        for(int i = 0; i<matrix.length; i++){
            for(int j = i; j<matrix[0].length; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i =0 ; i<matrix.length; i++){
            for(int j = 0; j<matrix.length/2; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length-1-j];
                matrix[i][matrix.length-1-j] = temp;
            }
        }
    }
}
"""
