"""
529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!
You are given a 2D char matrix representing the game board. 
'M' represents an unrevealed mine, 
'E' represents an unrevealed empty square, 
'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, 
digit ('1' to '8') represents how many mines are adjacent to this revealed square, 
'X' represents a revealed mine.

You are also given an integer array click where click = [clickr, clickc] represents 
the next click position among all the unrevealed squares ('M' or 'E').
Return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, 
then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') 
representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 
Example 1:
Input:
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
Click : [3,0]

Output: 
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Example 2:
Input: 
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
Click : [1,2]

Output: 
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Note:
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, 
you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr <= m
0 <= clickc <= n
board[clickr][clickc] is either 'M' or 'E'.
"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])

        def neighbors(i, j):
            for x, y in ((i-1,j), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j), (i+1,j-1), (i,j-1), (i-1,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y
        
        def dfs(i, j):
            mines = 0
            for x, y in neighbors(i, j):
                if board[x][y] == 'M':
                    mines += 1
            
            if mines != 0:
                board[i][j] = str(mines)
                return
            
            board[i][j] = 'B'
            for x, y in neighbors(i, j):
                if board[x][y] == 'E':
                    dfs(x, y)

        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else: # can be only 'M' or 'E'
            dfs(i, j)
        
        return board
        

sol = Solution()
print(sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3,0]))
print(sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [0,2]))
print(sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [0,4]))
print(sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [1,2]))
print(sol.updateBoard([["E","E","E","E","M"],["E","E","E","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [2,1]))

"""
My previous solution:

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        xCoords = [-1,-1,0,1,1,1,0,-1]
        yCoords = [0,1,1,1,0,-1,-1,-1]

        def dfs(i, j):
            count = 0
            for k in range(len(xCoords)):
                x, y = xCoords[k], yCoords[k]
                if i+x >= 0 and i+x < len(board) and j+y >= 0 and j+y < len(board[0]) and board[i+x][j+y] == 'M':
                    count += 1

            if count == 0: # reveal recursively
                board[i][j] = 'B'
                if i-1 >= 0 and board[i-1][j] == 'E':
                    dfs(i-1, j)
                if i-1 >= 0 and j+1 < len(board[0]) and board[i-1][j+1] == 'E':
                    dfs(i-1, j+1)
                if j+1 < len(board[0]) and board[i][j+1] == 'E':
                    dfs(i, j+1)
                if i+1 < len(board) and j+1 < len(board[0]) and board[i+1][j+1] == 'E':
                    dfs(i+1, j+1)
                if i+1 < len(board) and board[i+1][j] == 'E':
                    dfs(i+1, j)
                if i+1 < len(board) and j-1 >= 0 and board[i+1][j-1] == 'E':
                    dfs(i+1, j-1)
                if j-1 >= 0 and board[i][j-1] == 'E':
                    dfs(i, j-1)
                if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] == 'E':
                    dfs(i-1, j-1)
            else:
                board[i][j] = str(count)
            
            return

        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else: # can be only 'M' or 'E'
            dfs(i, j)

        return board 
"""
