"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
from typing import List


# Good explanation in leetcode solution: https://leetcode.com/problems/longest-common-subsequence/solution/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text1) for _ in range(len(text2))]
        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, len(text1)):
            if text2[0] == text1[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1]

        for i in range(1, len(text2)):
            if text1[0] == text2[i]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text2)-1][len(text1)-1]


sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))
print(sol.longestCommonSubsequence("abcde", "bce"))
print(sol.longestCommonSubsequence("abc", "abc"))
print(sol.longestCommonSubsequence("abc", "def"))
print(sol.longestCommonSubsequence("abc", "b"))
print(sol.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg"))


"""
Recursive solution:

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def longestCommonSubsequenceRecursive(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                res = longestCommonSubsequenceRecursive(i+1, j+1) + 1
            else:
                res = max(longestCommonSubsequenceRecursive(i+1, j), \
                    longestCommonSubsequenceRecursive(i, j+1))

            memo[(i, j)] = res
            return res
            
        return longestCommonSubsequenceRecursive(0, 0)
"""
