"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dict_of_words = dict()
        for word in wordDict:
            dict_of_words[word] = 1

        l = len(s)

        dp = [False] * (l + 1)
        dp[0] = True

        for i in range(1, l + 1):
            for j in range(i):
                if dp[j]:
                    string = s[j:i]
                    if string in dict_of_words:
                        dp[i] = True
                        # break

        return dp[l]

sol = Solution()
print(sol.wordBreak("leetcode", ["leet","code", "leetco", "co", "de"]))
print(sol.wordBreak("leetcode", ["leet","de", "leetcod"]))
