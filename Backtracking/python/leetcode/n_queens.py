"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""
from collections import defaultdict


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        rows, cols = [0] * n, [0] * n
        lDiag, rDiag = defaultdict(int), defaultdict(int)
        board = [['.'] * n for _ in range(n)]

        def setAttributes(i, j, val):
            rows[i] = val
            cols[j] = val
            lDiag[i-j] = val
            rDiag[i+j] = val
        
        def addBoard():
            solved = []
            for row in board:
                b = "".join(row)
                solved.append(b)
            res.append(solved)

        def solve(i):
            if i == n:
                addBoard()
                return
            
            for j in range(n):
                if rows[i] == 1 or cols[j] == 1 or lDiag[i-j] == 1 or rDiag[i+j] == 1:
                    continue
                
                board[i][j] = 'Q'
                setAttributes(i, j, 1)
                solve(i+1)
                board[i][j] = '.'
                setAttributes(i, j, 0)
        
        solve(0)
        return res


sol = Solution()
print(sol.solveNQueens(4))
print(sol.solveNQueens(1))
