"""
115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t:
            return 1
        elif not s:
            return 0

        dp = [[0] * len(s) for _ in range(len(t))]

        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, len(s)):
            if s[i] == t[0]:
                dp[0][i] = 1 + dp[0][i-1]
            else:
                dp[0][i] = dp[0][i-1]

        for i in range(1, len(t)):
            dp[i][0] = 0

        for i in range(1, len(t)):
            for j in range(1, len(s)):
                if t[i] == s[j]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[len(t)-1][len(s)-1]


sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))
print(sol.numDistinct("babgbag", "bag"))
print(sol.numDistinct("", "a"))
print(sol.numDistinct("a", "r"))
print(sol.numDistinct("a", ""))


'''
My dp recursive (top-down) solution:

class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t:
            return 1
        elif not s:
            return 0

        dp = [[float('inf')] * (len(t)+1) for _ in range(len(s)+1)]

        def distinct_recr(i, j):
            if dp[i][j] != float('inf'):
                return dp[i][j]
            if len(s) - i < len(t) - j:
                dp[i][j] = 0
            elif j == len(t):
                dp[i][j] = 1
            elif s[i] == t[j]:
                dp[i][j] = distinct_recr(i+1, j+1) + distinct_recr(i+1, j)
            else:
                dp[i][j] = distinct_recr(i+1, j)

            return dp[i][j]

        return distinct_recr(0, 0)
'''
