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
        paran_to_remove = []
        result = []

        for i, c in enumerate(s):
            if c == '(':
                paran_to_remove.append((c, i))
            elif c == ')':
                if paran_to_remove and paran_to_remove[-1][0] == '(':
                    paran_to_remove.pop()
                else:
                    paran_to_remove.append((c, i))

        start = 0
        for paran in paran_to_remove:
            result.append(s[start: paran[1]])
            start = paran[1] + 1
        result.append(s[start:])

        return "".join(result)


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

        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        # Note that s[::-1] gets the reverse of s.
        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]
"""
