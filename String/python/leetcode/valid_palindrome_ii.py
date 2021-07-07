"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(i, j, count):
            while i <= j:
                if s[i] != s[j]:
                    if count < 1:
                        if isValid(i+1, j, count+1) or isValid(i, j-1, count+1):
                            return True
                    break
                i += 1
                j -= 1

            return True if i > j else False

        return isValid(0, len(s)-1, 0)


sol = Solution()
print(sol.validPalindrome("aba"))
print(sol.validPalindrome("ac"))
print(sol.validPalindrome("abca"))
print(sol.validPalindrome("abc"))


"""
Leetcode discuss solution:

class Solution(object):
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
"""
