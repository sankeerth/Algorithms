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

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def neighbors(i, j, char):
            for x, y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == char:
                    yield x, y
        
        def backtrack(i, j, cur):
            if len(cur) > len(word):
                return False
            if cur == word:
                return True
            
            char = board[i][j]
            board[i][j] = "-"
            nextChar = word[len(cur)]

            for x, y in neighbors(i, j, nextChar):
                if backtrack(x, y, cur+nextChar):
                    return True
            
            board[i][j] = char
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, board[i][j]):
                        return True

        return False            


sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(sol.exist([["E","D","E"],["F","E","R"],["S","X","T"]], "ERTXS"))
print(sol.exist([["X","E","D"],["T","S","S"],["R","E","E"]], "ESSERT"))
print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))


"""
Complexity Analysis

Time Complexity: O(N * 3^L) where N is the number of cells in the board and L is the length of the word to be matched.

For the backtracking function, initially we could have at most 4 directions to explore, but further the choices 
are reduced into 3 (since we won't go back to where we come from). As a result, the execution trace after the first step 
could be visualized as a 3-ary tree, each of the branches represent a potential exploration in the corresponding direction.
Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree, which is about 3^L.

We iterate through the board for backtracking, i.e. there could be N times invocation for the backtracking function in the worst case.

As a result, overall the time complexity of the algorithm would be O(N * 3^L)

Space Complexity: O(L) where L is the length of the word to be matched.
The main consumption of the memory lies in the recursion call of the backtracking function. 
The maximum length of the call stack would be the length of the word.
"""

"""
class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        def dfs(i, j, index):
            if index == len(word):
                return True

            char = board[i][j]
            board[i][j] = '*'

            for x, y in neighbors(i, j):
                if board[x][y] == word[index]:
                    if dfs(x, y, index+1):
                        board[i][j] = char
                        return True
            
            board[i][j] = char
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False
"""
