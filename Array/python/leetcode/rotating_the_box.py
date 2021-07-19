"""
1861. Rotating the Box

You are given an m x n matrix of characters box representing a side-view of a box. 
Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.

Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 
Constraints:
m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
"""
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        res = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            j, k = cols-1, cols-1

            while j >= 0:
                if box[i][j] == '*':
                    while k > j:
                        box[i][k] = '.'
                        k -= 1
                    k -= 1
                elif box[i][j] == '#':
                    box[i][k] = '#'
                    k -= 1
                j -= 1

            while k >= 0:
                box[i][k] = '.'
                k -= 1

        # rotate by 90 degree
        for i in range(cols):
            for j in range(rows-1, -1, -1):
                k = rows-j-1 
                res[i][k] = box[j][i]
        
        return res


sol = Solution()
print(sol.rotateTheBox([["#",".","#"]]))
print(sol.rotateTheBox([["#",".","*","."], ["#","#","*","."]]))
print(sol.rotateTheBox([["#","#","*",".","*","."], ["#","#","#","*",".","."], ["#","#","#",".","#","."]]))
print(sol.rotateTheBox([["#",".","*","#","."],["#","#","*","#","#"]])) # imp testcase
