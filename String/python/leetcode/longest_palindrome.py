"""
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        result = 0
        char_count = Counter(s)
        for count in char_count.values():
            if count % 2 == 0:
                result += count
            else:
                result += (count - 1)

        return result + 1 if result < len(s) else result


sol = Solution()
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome("aaccccdd"))
print(sol.longestPalindrome("abcdegjl"))
print(sol.longestPalindrome("abcadefg"))
print(sol.longestPalindrome("aaaabbbccc"))
