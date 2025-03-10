"""
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

Constraints:
0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(i):
            string = ""
            while i < len(s):
                c = s[i]
                if c == "(":
                    i, r = reverse(i+1)
                    string += r
                elif c == ")":
                    return i, string[::-1]
                else:
                    string += c
                i += 1
            return string
        
        return reverse(0)


s = Solution()
print(s.reverseParentheses("(abcd)"))
print(s.reverseParentheses("(u(love)i)"))
print(s.reverseParentheses("(ed(et(oc))el)"))
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))


"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        for c in s:
            if c == ')':
                temp = []
                while res[-1] != '(':
                    temp.append(res.pop())
                res.pop()
                res += temp
            else:
                res.append(c)
        
        return "".join(res)
"""
