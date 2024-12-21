"""
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Example 4:
Input: s = "+48 + -48"
Output: 0
Explanation: Numbers can have multiple digits and start with +/-. 

Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
Every number and running calculation will fit in a signed 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        operators = {'+', '-'}

        def append(num, op, stack):
            if op == '-':
                num = -1 * num
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
                
                if cur in operators or i == len(s)-1:
                    append(num, op, stack)
                    op = cur
                    num = 0
                
                i += 1
            
            return sum(stack)

        return calc(0)


sol = Solution()
print(sol.calculate("1 + 1 "))
print(sol.calculate(" 2-1 + 2 "))
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("(1-(4-5+2)-3)"))
print(sol.calculate("1-(4-5+2)"))
print(sol.calculate("+48 + -48"))


"""
My other solution with two stacks:

class Solution:
    def calculate(self, s: str) -> int:
        ops = {"+","-"}
        def evaluate(numbers, operators):
            c = 0
            while len(numbers) >= 2:
                a = numbers.popleft()
                b = numbers.popleft()
                op = operators.popleft()
                
                if op == "+":
                    c = a + b
                elif op == "-":
                    c = a - b
                numbers.appendleft(c)

            return numbers[-1]

        def calc(i):
            numbers, operators = deque(), deque()
            num = 0

            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = 10 * num + int(c)
                elif c in ops:
                    numbers.append(num)
                    operators.append(c)
                    num = 0
                elif c == "(":
                    i, r = calc(i+1)
                    num += r
                elif c == ")":
                    numbers.append(num)
                    return i, evaluate(numbers, operators)
                
                if i == len(s)-1:
                    numbers.append(num)

                i += 1
            
            return evaluate(numbers, operators)

        return calc(0)
"""
