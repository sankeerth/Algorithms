"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

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

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]

        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                elif s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]

        return dp[len(s1)][len(s2)]


sol = Solution()
print(sol.isInterleave("ab", "bc", "babc"))
print(sol.isInterleave("ab", "cbd", "acbbd"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))


'''
My dp recursive (top-down) solution:

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def isInterleaveRecursive(i, j):
            if i == len(s1):
                return s2[j:] == s3[i+j:]
            elif j == len(s2):
                return s1[i:] == s3[i+j:]
            elif (i, j) in memo:
                return memo[(i, j)]

            res = False
            if s1[i] == s2[j] == s3[i+j]:
                res = isInterleaveRecursive(i+1, j) or isInterleaveRecursive(i, j+1)
            elif s1[i] == s3[i+j]:
                res = isInterleaveRecursive(i+1, j)
            elif s2[j] == s3[i+j]:
                res = isInterleaveRecursive(i, j+1)

            memo[(i, j)] = res
            return res
        
        return isInterleaveRecursive(0, 0)
'''
