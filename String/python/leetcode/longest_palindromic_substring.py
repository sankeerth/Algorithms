"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        result = s[0]
        l = len(s) - 1
        max_len = 1

        def len_of_palindrome(j, k, l):
            while j >= 0 and k <= l and s[j] == s[k]:
                j -= 1
                k += 1

            return j + 1, k - 1

        for i in range(l):
            j, k = len_of_palindrome(i - 1, i + 1, l)
            if (k - j + 1) > max_len:
                max_len = k - j + 1
                result = s[j:k + 1]

            if s[i] == s[i + 1]:
                j, k = len_of_palindrome(i - 1, i + 2, l)
                if (k - j + 1) > max_len:
                    max_len = k - j + 1
                    result = s[j:k + 1]

        return result

sol = Solution()
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("baabad"))
print(sol.longestPalindrome("baabaaba"))
print(sol.longestPalindrome("baabaabaa"))
print(sol.longestPalindrome("bdcaaa"))

'''
My Dynamic programming solution

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0

        length = len(s)
        dp = [([False] * length) for _ in range(length)]

        for i in range(length):
            dp[i][i] = True

        result = s[0]

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    if j == i+1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        result = s[i:j+1] if j-i+1 > len(result) else result
                else:
                    dp[i][j] = False

        return result
'''

'''
My dp recursive (top-down) solution:

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        result = s[0]
        max_len = 1

        dp = [[float('inf')] * len(s) for _ in range(len(s))]

        def longest_palidrome_recr(i, j):
            nonlocal result
            nonlocal max_len

            if dp[i][j] != float('inf'):
                return dp[i][j]
            elif i == j:
                dp[i][j] = True
            elif i > j:
                dp[i][j] = True
            elif s[i] == s[j]:
                longest_palidrome_recr(i + 1, j - 1) or longest_palidrome_recr(i, j - 1) or longest_palidrome_recr(i + 1, j)
                dp[i][j] = dp[i+1][j-1]
            else:
                longest_palidrome_recr(i, j-1) or longest_palidrome_recr(i+1, j)
                dp[i][j] = False

            if dp[i][j] is True and j-i+1 > max_len:
                max_len = j-i+1
                result = s[i:j+1]

            return dp[i][j]

        longest_palidrome_recr(0, len(s)-1)
        return result
'''
