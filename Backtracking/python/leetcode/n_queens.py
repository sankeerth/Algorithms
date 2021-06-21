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
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []

        def solve(i, horizontal, vertical, lOblique, rOblique):
            if i == n:
                if len(horizontal) == n:
                    temp = []
                    for row in board:
                        temp.append(''.join(row))
                    res.append(temp)
                return
            
            for j in range(n):
                if i not in horizontal and j not in vertical and j-i not in lOblique and i+j not in rOblique:
                    board[i][j] = 'Q'
                    horizontal.add(i)
                    vertical.add(j)
                    lOblique.add(j-i)
                    rOblique.add(i+j)

                    solve(i+1, horizontal, vertical, lOblique, rOblique)
                    board[i][j] = '.'
                    horizontal.remove(i)
                    vertical.remove(j)
                    lOblique.remove(j-i)
                    rOblique.remove(i+j)


        solve(0, set(), set(), set(), set())
        return res


sol = Solution()
print(sol.solveNQueens(4))
print(sol.solveNQueens(1))
