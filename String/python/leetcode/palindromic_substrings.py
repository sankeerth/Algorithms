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
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        length = len(s)
        dp = [([False] * length) for _ in range(length)]

        for i in range(length):
            dp[i][i] = True

        result = length

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    if j == i+1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        result += 1
                else:
                    dp[i][j] = False

        return result


sol = Solution()
print(sol.countSubstrings("aaa"))
print(sol.countSubstrings("abc"))
print(sol.countSubstrings("abca"))
print(sol.countSubstrings("abdadba"))
