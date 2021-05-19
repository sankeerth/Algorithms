"""
730. Count Different Palindromic Subsequences

Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.
A subsequence of a string S is obtained by deleting 0 or more characters from S.
A sequence is palindromic if it is equal to the sequence reversed.
Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input:
S = 'bccb'
Output: 6
Explanation:
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:
Input:
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation:
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:
The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        mod = 1000000007
        dp = [[0] * length for _ in range(length)]

        for i in range(length):
            dp[i][i] = 1

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if s[i] != s[j]:
                    dp[i][j] = (dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]) % mod
                else:
                    dp[i][j] = (2 * dp[i+1][j-1]) % mod
                    l, r = i + 1, j-1

                    while l <= r and s[i] != s[l]:
                        l += 1
                    while l <= r and s[i] != s[r]:
                        r -= 1

                    if l > r:
                        dp[i][j] = (2 + dp[i][j]) % mod
                    elif l == r:
                        dp[i][j] = (1 + dp[i][j]) % mod
                    elif r - l >= 2:
                        dp[i][j] = (dp[i][j] - dp[l+1][r-1]) % mod

                dp[i][j] = (dp[i][j] + mod) % mod

        return dp[0][length-1]


sol = Solution()
print(sol.countPalindromicSubsequences("bccb"))
print(sol.countPalindromicSubsequences("babab"))
print(sol.countPalindromicSubsequences("babac"))
print(sol.countPalindromicSubsequences("aaaa"))
print(sol.countPalindromicSubsequences("abdad"))
print(sol.countPalindromicSubsequences("bdadb"))
print(sol.countPalindromicSubsequences("abdadba"))
