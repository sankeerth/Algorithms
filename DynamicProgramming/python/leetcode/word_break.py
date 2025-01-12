"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
You may assume the dictionary does not contain duplicate words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""
from typing import List


# Backward DP (easier)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set()
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for word in wordDict:
            wordset.add(word)

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                prefix = s[i:j]
                if prefix in wordset and dp[j]:
                    dp[i] = True
                    break

        return dp[0]


sol = Solution()
print(sol.wordBreak("leetcode", ["leet","code", "leetco", "co", "de"]))
print(sol.wordBreak("leetcode", ["leet","de", "leetcod"]))
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaad", ["a","aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaaaaa"]))
print(sol.wordBreak("aaaad", ["a","aa", "aaa", "aaaa"]))
print(sol.wordBreak("code", ["c", "od"]))
print(sol.wordBreak("dba", ["d", "ab"]))
print(sol.wordBreak("c", ["d", "a"]))
print(sol.wordBreak("applepenapple", ["apple", "pen"]))
print(sol.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"]))


"""
# Forward DP:

class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j]:
                    string = s[j:i]
                    if string in wordSet:
                        dp[i] = True
                        break

        return dp[len(s)]
"""

"""
# Recursive solution:

class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        memo = [-1] * len(s)

        def wordBreakRecursive(i):
            if s[i:] == "" or s[i:] in wordSet:
                return True

            if memo[i] != -1:
                return memo[i]

            res = False
            for j in range(i, len(s)):
                # and memo[j+1] can be added in the if condition below which will avoid 
                # a recursive call when it is already computed as False since m[j]==-1 will be True.
                word = s[i:j+1]
                if word in wordSet:
                    res = wordBreakRecursive(j+1)
                    if res:
                        break

            memo[i] = res
            return res

        return wordBreakRecursive(0)
"""
