"""
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i+1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
        
        return res


sol = Solution()
print(sol.countSubstrings("aaa"))
print(sol.countSubstrings("abc"))
print(sol.countSubstrings("abca"))
print(sol.countSubstrings("abdadba"))


'''
Another dp solution:

class Solution(object):
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        dp = [([0] * length) for _ in range(length)]

        for i in range(length):
            dp[i][i] = 1

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]

        return dp[0][length-1]
'''
