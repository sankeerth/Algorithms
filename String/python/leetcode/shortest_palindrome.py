"""
214. Shortest Palindrome

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:
Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".
"""

"""
Leetcode solution using KMP table. See discuss for explanation.
"""


class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [0]
        def prefix(s):
            nonlocal res
            border = 0
            for i in range(1, len(s)):
                while border > 0 and s[i] != s[border]:
                    border = res[border - 1]
                border = border + 1 if s[i] == s[border] else 0
                res.append(border)
        prefix(s + '#' + s[::-1])
        return s[res[-1]:][::-1] + s


sol = Solution()
print(sol.shortestPalindrome("abadc"))
print(sol.shortestPalindrome("aba"))
print(sol.shortestPalindrome("aaa"))
print(sol.shortestPalindrome("abcd"))
print(sol.shortestPalindrome("aacecaaa"))


'''
My Solution:
class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(string):
            return string == string[::-1]
        
        append_front = ""
        for i in range(len(s), -1, -1):
            if is_palindrome(s[:i]):
                append_front = s[i:][::-1]
                break
            
        result = append_front + s
        return result
'''
