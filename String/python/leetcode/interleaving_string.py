"""
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Why is this a DP problem and why can't it be solved recursively?
Ex:
s1 = "aaaa"
s2 = "aaaa"
s3 = "aaaaaaab"

Every char of s3 can be formed by either char of s1 or s2. There are 2 choices for almost every character and it reaches
exponential very soon
"""


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(1, len(s2)+1):
            dp[0][i] = s3[i-1] == s2[i-1] and dp[0][i-1]

        for i in range(1, len(s1)+1):
            dp[i][0] = s3[i-1] == s1[i-1] and dp[i-1][0]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = s3[i+j-1] == s1[i-1] and dp[i-1][j] or s3[i+j-1] == s2[j-1] and dp[i][j-1]

        return dp[len(s1)][len(s2)]


sol = Solution()
print(sol.isInterleave("ab", "cbd", "acbbd"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))


'''
My dp recursive (top-down) solution:

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[float('inf')] * (len(s2)+1) for _ in range(len(s1)+1)]

        def interleave_recr(i, j):
            if i == len(s1) and j == len(s2):
                return True
            elif dp[i][j] != float('inf'):
                return dp[i][j]
            elif i == len(s1):
                dp[i][j] = s2[j] == s3[i+j] and interleave_recr(i, j+1)
            elif j == len(s2):
                dp[i][j] = s1[i] and s3[i+j] and interleave_recr(i+1, j)
            elif s1[i] == s2[j] == s3[i+j]:
                dp[i][j] = interleave_recr(i+1, j) or interleave_recr(i, j+1)
            elif s1[i] == s3[i+j]:
                dp[i][j] = interleave_recr(i+1, j)
            elif s2[j] == s3[i+j]:
                dp[i][j] = interleave_recr(i, j+1)
            else:
                return False

            return dp[i][j]

        return interleave_recr(0, 0)
'''
