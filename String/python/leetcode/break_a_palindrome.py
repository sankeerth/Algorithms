"""
1328. Break a Palindrome

Given a palindromic string palindrome, replace exactly one character by any lowercase 
English letter so that the string becomes the lexicographically smallest possible 
string that isn't a palindrome.
After doing so, return the final string.  If there is no way to do so, return 
the empty string.

Example 1:
Input: palindrome = "abccba"
Output: "aaccba"

Example 2:
Input: palindrome = "a"
Output: ""

Constraints:
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(int(len(palindrome)/2)):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            
        return palindrome[:-1] + 'b' if palindrome[:-1] else ""
        

s = Solution()
print(s.breakPalindrome("a"))
print(s.breakPalindrome("b"))
print(s.breakPalindrome("abccba"))
print(s.breakPalindrome("aba"))
print(s.breakPalindrome("abba"))
print(s.breakPalindrome("aabaa"))


"""
My solution:

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        l = list(palindrome)
        s = set(l)
        
        if len(s) == 1 and 'a' in s:
            l[-1] = 'b'
            return "".join(l)
        
        for i in range(len(l)):
            if l[i] != 'a':
                cur = l[i]
                l[i] = 'a'
                if len(set(l)) == 1:
                    l[i] = cur
                    l[-1] = 'b'
                break
                
        return "".join(l)
"""
