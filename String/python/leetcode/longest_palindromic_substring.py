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

        for i in range(1, l):
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
