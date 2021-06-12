"""
289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array 
(i.e., live cells reach the border). How would you address these problems?
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        nextStage = [[0] * cols for _ in range(rows)]

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1), (i-1,j-1), (i-1,j+1), (i+1,j+1), (i+1,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        for i in range(rows):
            for j in range(cols):
                ones, zeros = 0, 0
                cur = board[i][j]
                for x, y in neighbors(i, j):
                    if board[x][y] == 0:
                        zeros += 1
                    else:
                        ones += 1

                if cur == 1 and ones < 2:
                    nextStage[i][j] = 0
                elif cur == 1 and 1 < ones < 4:
                    nextStage[i][j] = 1
                elif cur == 1 and ones > 3:
                    nextStage[i][j] = 0
                elif cur == 0 and ones == 3:
                    nextStage[i][j] = 1

        for i in range(rows):
            for j in range(cols):
                board[i][j] = nextStage[i][j]

        return board


sol = Solution()
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print(sol.gameOfLife([[1,1],[1,0]]))


"""
In place:
1 -> -1 instead of 0 when it turns to dead cell and 0->2 instead of 1 when it turns to live cell

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1), (i-1,j-1), (i-1,j+1), (i+1,j+1), (i+1,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        for i in range(rows):
            for j in range(cols):
                ones, zeros = 0, 0
                cur = board[i][j]
                for x, y in neighbors(i, j):
                    if abs(board[x][y]) == 1:
                        ones += 1
                    else:
                        zeros += 1

                if cur == 1 and ones < 2:
                    board[i][j] = -1
                elif cur == 1 and 1 < ones < 4:
                    board[i][j] = 1
                elif cur == 1 and ones > 3:
                    board[i][j] = -1
                elif cur == 0 and ones == 3:
                    board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
"""
