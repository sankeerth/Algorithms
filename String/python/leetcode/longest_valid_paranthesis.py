"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Example 3:
Input: s = ""
Output: 0

Constraints:
    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        
        open, close, left = 0, 0, 0
        for right, c in enumerate(s):
            if c == ')':
                if close < open:
                    close += 1
                else:
                    left = right+1
            else:
                open += 1
            
            if open == close:
                res = max(res, right-left+1)

        open, close, right = 0, 0, len(s)-1
        for left in range(len(s)-1, -1, -1):
            c = s[left]
            if c == '(':
                if open < close:
                    open += 1
                else:
                    right = left-1
            else:
                close += 1

            if open == close:
                res = max(res, right-left+1)
        
        return res


sol = Solution()
print(sol.longestValidParentheses("(()"))
print(sol.longestValidParentheses(")()())"))
print(sol.longestValidParentheses("(()()("))
print(sol.longestValidParentheses(")(()())"))
print(sol.longestValidParentheses("(()(()()(("))
print(sol.longestValidParentheses("("))
print(sol.longestValidParentheses(")"))
print(sol.longestValidParentheses(""))


"""
My other solution using the same code but reversing the strings:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        if not s:
            return 0

        def longest_valid_parantheses(s, par):
            nonlocal result
            op = 0
            prev = -1
            for i in range(len(s)):
                if s[i] == par[0]:
                    op += 1
                elif s[i] == par[1]:
                    op -= 1

                if op < 0:
                    prev = i
                    op = 0
                elif op == 0:
                    result = max(result, i - prev)

        longest_valid_parantheses(s, ['(', ')'])
        longest_valid_parantheses(s[::-1], [')', '('])

        return result
"""
