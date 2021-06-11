"""
772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1+1"
Output: 2

Example 2:
Input: s = "6-4/2"
Output: 4

Example 3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 4:
Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12

Example 5:
Input: s = "0"
Output: 0

Constraints:
1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.
"""


class Solution:
    def calculate(self, s: str) -> int:
        operators = {'+', '-', '*', '/'}

        def append(num, op, stack):
            if op == '-':
                num = -1 * num
            elif op == '*':
                num = stack.pop() * num
            elif op == '/':
                num = int(stack.pop() / num)
            stack.append(num)
        
        def calc(i):
            stack = []
            op, num = "+", 0
            while i < len(s):
                cur = s[i]
                if cur == '(':
                    i, num = calc(i+1)
                elif cur == ')':
                    append(num, op, stack)
                    return i, sum(stack)
                elif cur.isdigit():
                    num = 10 * num + int(cur)
                
                if cur in operators or i == len(s)-1: # so that num is appended to stack at the end of string
                    append(num, op, stack)
                    op = cur
                    num = 0
                
                i += 1
            
            return sum(stack)

        return calc(0)


sol = Solution()
print(sol.calculate("1+1"))
print(sol.calculate("6-4/2"))
print(sol.calculate("2*(5+5*2)/3+(6/2+8)"))
print(sol.calculate("(2+6*3+5-(3*14/7+2)*5)+3"))
