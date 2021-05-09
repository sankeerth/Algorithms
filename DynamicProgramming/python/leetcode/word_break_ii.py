"""
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to 
construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

Constraints:
    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        startCharToWords, memo = dict(), dict()
        for word in wordDict:
            start = word[0]
            if not start in startCharToWords:
                startCharToWords[start] = []
            startCharToWords[start].append(word)

        def wordBreakRecursive(s):
            if not s or s[0] not in startCharToWords:
                return []

            if s in memo:
                return memo[s]
            
            res = []
            for word in startCharToWords[s[0]]:
                if s.startswith(word):
                    if len(word) == len(s):
                        res.append(word)
                        break
                    sublist = wordBreakRecursive(s[len(word):])
                    for item in sublist:
                        res.append(word + ' ' + item)
                        
            memo[s] = res
            return res

        return wordBreakRecursive(s)


s = Solution()
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "doge"]))
print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak("bb", ["a","b","bbb","bbbb"]))
print(s.wordBreak("bb", ["a","b","bbb","bbbb", "bb"]))
print(s.wordBreak("aaaaabaaa", ["a","aa","aaa","aaaa","aaaaa"]))
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))


"""
Iterative solution:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False] * (len(s)+1)
        memo = [[] for _ in range(len(s)+1)]
        dp[-1] = True
        wordSet = set(wordDict)

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                prefix = s[i:j]
                if prefix in wordSet and dp[j]:
                    dp[i] = True
                    if not memo[j]:
                        memo[i].append(prefix)
                    else:
                        for word in memo[j]:
                            memo[i].append(prefix + ' ' + word)

        return memo[0]
"""

"""
Time limit exceeded for Trie based solution for test case:
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        class Trie:
            def __init__(self, char):
                self.char = char
                self.d = dict()
                self.wordEnd = False

            def __repr__(self):
                return "Trie({})".format(self.char)

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

        def buildTrie(root):
            for word in wordDict:
                node = root
                for char in word:
                    if not node.isOrGetChild(char):
                        node.addChild(char)
                    node = node.isOrGetChild(char)
                node.setWordEnd(True)

        root = Trie('')
        buildTrie(root)
        result = []

        def wordBreakRecursive(s, node, wordList):
            if s == '':
                if node.isWordEnd(): # append only if end of word
                    result.append(''.join(wordList))
                return
            
            char = s[0]
            child = node.isOrGetChild(char)
            if not child:
                return

            wordList.append(char)
            if child.isWordEnd() and len(s) > 1:
                wordList.append(' ')
                wordBreakRecursive(s[1:], root, wordList)
                wordList.pop()
            
            wordBreakRecursive(s[1:], child, wordList)
            wordList.pop()

        wordBreakRecursive(s, root, [])
        return result
"""

"""
My recursive solution still does not work! Not sure why!! 
Update: Leetcode has reduced the constraints: 1 <= s.length <= 20
However, keeping the below solution I had tried for posterity

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        startCharToWords, memo = dict(), dict()
        result = []

        for word in wordDict:
            start = word[0]
            if not start in startCharToWords:
                startCharToWords[start] = []
            startCharToWords[start].append(word)

        def wordBreakRecursive(s):
            if not s or s[0] not in startCharToWords:
                return [[]]

            if s in memo:
                return memo[s]
            
            start = s[0]
            res = []
            for word in startCharToWords[start]:
                if s.startswith(word):
                    sublist = wordBreakRecursive(s[len(word):])
                    for sub in sublist:
                        res.append([word] + sub)

            memo[s] = res
            return res

        wordBreaks = wordBreakRecursive(s)
        
        for wordBreak in wordBreaks:
            result.append(' '.join(wordBreak))

        return result

"""
