"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res, paranToRemove = [], []

        for i, c in enumerate(s):
            if c == '(':
                paranToRemove.append((c, i))
            elif c == ')':
                if paranToRemove and paranToRemove[-1][0] == '(':
                    paranToRemove.pop()
                else:
                    paranToRemove.append((c, i))

        start = 0
        for _, i in paranToRemove:
            res.append(s[start:i])
            start = i + 1
        res.append(s[start:])

        return "".join(res)


s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a(b(c)d)"))
print(s.minRemoveToMakeValid("))(("))
print(s.minRemoveToMakeValid("a)b(c)d"))


"""
Leetcode solution: Two pass but a different variant where string is parsed from left to right
to remove invalid ')' and parsed from right to left to remove invalid '('.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:        
        def removeInvalid(string, openP, closeP):
            res = []
            count = 0
            for c in string:
                if c == openP:
                    count += 1
                elif c == closeP:
                    if count == 0:
                        continue
                    count -= 1
                res.append(c)
            
            return "".join(res)
        
        res = removeInvalid(s, '(', ')')
        res = removeInvalid(res[::-1], ')', '(')
        return res[::-1]
"""
