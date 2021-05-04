"""
212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent 
cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self, char):
                self.char = char
                self.d = dict()
                self.wordEnd = False

            def __repr__(self):
                return "Trie({})".format(self.char)

            def getChar(self):
                return self.char

            def addChild(self, char):
                if not char in self.d:
                    child = Trie(char)
                    self.d[char] = child

            def isOrGetChild(self, char): # returns child Trie node or None
                if char in self.d:
                    return self.d[char]
                return None

            def isWordEnd(self):
                return self.wordEnd

            def setWordEnd(self, wordEnd):
                self.wordEnd = wordEnd

        result = set()
        rows, cols = len(board), len(board[0])
        root = Trie('')

        def buildTrie(root):
            for word in words:
                node = root
                for char in word:
                    if not node.isOrGetChild(char):
                        node.addChild(char)
                    node = node.isOrGetChild(char)
                node.wordEnd = True

        def dfs(i, j, node, wordList):
            if node.isWordEnd():
                result.add("".join(wordList))
  
            cur = board[i][j]
            board[i][j] = '*'

            for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    child = node.isOrGetChild(board[x][y])
                    if child:
                        wordList.append(board[x][y])
                        dfs(x, y, child, wordList)

            board[i][j] = cur
            wordList.pop()

        buildTrie(root)
        for i in range(rows):
            for j in range(cols):
                child = root.isOrGetChild(board[i][j])
                if child:
                    dfs(i, j, child, [child.getChar()])

        return list(result)


s = Solution()
print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(s.findWords([["o","a","a","n"],["a","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(s.findWords([["a","b"],["c","d"]], ["abcb"]))
print(s.findWords([["a","b"]], ["ab"]))
print(s.findWords([["b"]], ["ab"]))
print(s.findWords([["b"]], ["b"]))
print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","ath","eth","at", "eak", "eah"]))


"""
Complexity

Time complexity: O(M * 4⋅3^L−1), where M is the number of cells in the board and L is the maximum length of words.
It is tricky is calculate the exact number of steps that a backtracking algorithm would perform. 
We provide a upper bound of steps for the worst scenario for this problem. The algorithm loops over all the cells in the board, 
therefore we have MM as a factor in the complexity formula. It then boils down to the maximum number of steps we would need for 
each starting cell (i.e 4⋅3^L−1).

Assume the maximum length of word is L, starting from a cell, initially we would have at most 4 directions to explore. 
Assume each direction is valid (i.e. worst case), during the following exploration, we have at most 3 neighbor cells 
(excluding the cell where we come from) to explore. As a result, we would traverse at most 
4⋅3^L−1 cells during the backtracking exploration.

One might wonder what the worst case scenario looks like. Well, here is an example. Imagine, each of the cells in the board 
contains the letter a, and the word dictionary contains a single word ['aaaa']. 

Note that, the above time complexity is estimated under the assumption that the Trie data structure would not change once built. 
If we apply the optimization trick to gradually remove the nodes in Trie, we could greatly improve the time complexity, 
since the cost of backtracking would reduced to zero once we match all the words in the dictionary, i.e. the Trie becomes empty.

Space Complexity: O(N), where N is the total number of letters in the dictionary.
The main space consumed by the algorithm is the Trie data structure we build. In the worst case where there is no overlapping of 
prefixes among the words, the Trie would have as many nodes as the letters of all words. 
And optionally, one might keep a copy of words in the Trie as well. As a result, we might need 2N2N space for the Trie.
"""

"""
Leetcode solution:

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = True

        result = []
        def backtrack(i: int, j: int, node = trie, prefix: str = ''):
            letter = board[i][j]
            if letter in node:
                board[i][j] = '#'
                node = node[letter]
                if '$' in node:
                    result.append(prefix + letter)
                    del node['$']
                for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= r < rows and 0 <= c < cols:
                        backtrack(r, c, node, prefix + letter)
                board[i][j] = letter

        for i in range(rows):
            for j in range(cols):
                backtrack(i, j)

        return result
"""

"""
Leetcode discuss solution using Complex Numbers:

I first build the tree of words with root root and also represent the board a different way, 
namely as one-dimensional dictionary where the keys are complex numbers representing the row/column indexes. 
That makes further work with it easier. Looping over all board positions is just for z in board, 
the four neighbors of a board position z are just z + 1j**k (for k in 0 to 3), and 
I don't need to check borders because board.get just returns "None" if I request an invalid position.

After this preparation, I just take the tree and recursively dive with it into each board position. 
Similar to how you'd search a single word, but with the tree instead.

class Solution:
    def findWords(self, board, words):

        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')

        return found
"""

"""
Tried solving without a Trie, using set, to see if it gets accepted.
Solution was not accepted (39/40) - TLE

class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res, seen = [], set()
        startCharToWords = defaultdict(set)

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        def dfs(i, j, cur, start):
            if cur in startCharToWords[start] and cur not in seen:
                res.append(cur)
                seen.add(cur)

            char = board[i][j]
            board[i][j] = '*'

            index = len(cur)
            for x, y in neighbors(i, j):
                for word in startCharToWords[start]:
                    if word not in seen and index < len(word) and board[x][y] == word[index]:
                        dfs(x, y, cur + board[x][y], start)
            
            board[i][j] = char

        for word in words:
            startCharToWords[word[0]].add(word)

        for i in range(rows):
            for j in range(cols):
                if len(seen) == len(words):
                    break
                if board[i][j] in startCharToWords:
                    dfs(i, j, board[i][j], board[i][j])

        return res
"""
