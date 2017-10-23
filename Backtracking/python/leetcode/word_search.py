"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
from collections import defaultdict


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        word_len = len(word)
        if word_len == 0:
            return True

        if not board:
            return False

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True

            char = board[i][j]
            board[i][j] = '*'

            if i > 0 and board[i - 1][j] == word[index]:
                if dfs(i - 1, j, index + 1):
                    return True
            if j > 0 and board[i][j - 1] == word[index]:
                if dfs(i, j - 1, index + 1):
                    return True
            if i < rows - 1 and board[i + 1][j] == word[index]:
                if dfs(i + 1, j, index + 1):
                    return True
            if j < cols - 1 and board[i][j + 1] == word[index]:
                if dfs(i, j + 1, index + 1):
                    return True

            board[i][j] = char
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False

sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(sol.exist([["E","D","E"],["F","E","R"],["S","X","T"]], "ERTXS"))
print(sol.exist([["X","E","D"],["T","S","S"],["R","E","E"]], "ESSERT"))
print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
