"""
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        length = len(s)
        dp = [([1] * length) for _ in range(length)]

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    if j == i+1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][length-1]


sol = Solution()
print(sol.longestPalindromeSubseq("cbbd"))
print(sol.longestPalindromeSubseq("a"))
print(sol.longestPalindromeSubseq("bbbab"))
print(sol.longestPalindromeSubseq("abda"))
