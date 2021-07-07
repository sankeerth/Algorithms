"""
1216. Valid Palindrome III

Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it. 

Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.

Example 2:
Input: s = "abbababa", k = 1
Output: true

Constraints:
1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}

        def isValid(i, j, count):
            if (i,j,count) in memo:
                return memo[(i,j,count)]

            while i <= j:
                if s[i] != s[j]:
                    if count < k:
                        if isValid(i+1, j, count+1) or isValid(i, j-1, count+1):
                            return True
                    break
                i += 1
                j -= 1

            res = True if i > j else False
            memo[(i,j,count)] = res
            return res
            

        return isValid(0, len(s)-1, 0)


sol = Solution()
print(sol.isValidPalindrome("abcdeca", 2))
print(sol.isValidPalindrome("abbababa", 1))
