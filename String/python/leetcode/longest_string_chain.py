"""
1048. Longest String Chain

You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA 
without changing the order of the other characters to make it equal to wordB.
For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, 
and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        res = 0
        words.sort(reverse=True, key=lambda x: len(x))
        wordSet, seen = set(words), set()

        def bfs(word):
            chain = 1
            queue = [(word, 1)]
            seen.add(word)

            while queue:
                word, count = queue.pop(0)
                chain = max(chain, count)
                # was initially here and gave TLE since the same word can be added to queue multiple times
                # ex: abcd -> (abc, abd, bcd) -> (ab, ab) -> (a, a), ab is repeated
                # since the first time we encounter the word is the best possible result, so we can add it to seen earlier
                # seen.add(word)

                for i in range(len(word)):
                    s = word[:i] + word[i+1:]
                    if s in wordSet and s not in seen:
                        seen.add(s)
                        queue.append((s, count+1))

            return chain

        for word in words:
            if word not in seen:
                chain = bfs(word)
                res = max(res, chain)

        return res


sol = Solution()
print(sol.longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(sol.longestStrChain(["abcd","dbqca"]))
print(sol.longestStrChain(["a","v", "x"]))
