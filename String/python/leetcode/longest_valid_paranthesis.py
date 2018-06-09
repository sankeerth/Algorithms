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
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        # forwards
        i, j = 0, 0
        current_sum = 0

        while i < len(s) and j < len(s):
            current_sum = current_sum + 1 if s[j] == '(' else current_sum - 1
            if current_sum < 0:
                i = j + 1
                j = i
                current_sum = 0
            elif current_sum == 0:
                result = max(result, j-i+1)
                j += 1
            else:
                j += 1

        # backwards
        i, j = len(s)-1, len(s)-1
        current_sum = 0

        while i > 0 and j > 0:
            current_sum = current_sum + 1 if s[j] == '(' else current_sum - 1
            if current_sum > 0:
                i = i - 1
                j = i
                current_sum = 0
            elif current_sum == 0:
                result = max(result, i-j+1)
                j -= 1
            else:
                j -= 1

        return result


sol = Solution()
print(sol.longestValidParentheses("(()"))
print(sol.longestValidParentheses(")()())"))
print(sol.longestValidParentheses("(()()("))
print(sol.longestValidParentheses(")(()())"))
print(sol.longestValidParentheses("(()(()()(("))
print(sol.longestValidParentheses("("))
print(sol.longestValidParentheses(")"))
print(sol.longestValidParentheses(""))


'''
My other simpler solution by using the same code but reversing the strings:

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
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
'''