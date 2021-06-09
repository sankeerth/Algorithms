"""
419. Battleships in a Board

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, 
empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, 
they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example 1:
X..X
...X
...X
Output: 2

Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Example 2:
Input: board = [["."]]
Output: 0

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is either '.' or 'X'.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (j-1 >= 0 and board[i][j-1] == 'X') or (i-1 >= 0 and board[i-1][j] == 'X'):
                        continue
                    res += 1
        
        return res


s = Solution()
print(s.countBattleships([["X",".",".","X"],[".","X",".","X"],[".","X",".","X"]]))


"""
# BFS with Queue

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    q = [(i, j)]
                    while q:
                        r, c = q.pop(0)
                        board[r][c] = '#'
                        for x, y in directions:
                            nr = r + x
                            nc = c + y
                            if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]) and board[nr][nc]=='X':
                                q.append((nr, nc))

                    res +=1
        return res
"""

"""
# DFS recursively

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    self.dfs(board, i ,j)
                    res +=1
        return res
    
    def dfs(self, board, i, j):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='X':
            return
        
        board[i][j]='#'
        
        self.dfs(board, i+1,j)
        self.dfs(board, i-1, j)
        self.dfs(board,i,j+1)
        self.dfs(board, i, j-1)
"""
