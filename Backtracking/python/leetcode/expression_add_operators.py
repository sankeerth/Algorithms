"""
282. Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to add the 
binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Example 3:
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:
Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]

Example 5:
Input: num = "3456237490", target = 9191
Output: []

Constraints:
1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
"""
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if target > 0 and int(num) == target:
            return [num]

        operators = ['+', '-', '*']
        n, res = len(num), []
        def evaluate(expression):
            stack = []
            cur, op = 0, '+'

            for i, e in enumerate(expression):
                if e.isdigit():
                    cur = int(e)
                if e in operators or i == len(expression)-1:
                    if op == '+':
                        stack.append(cur)
                    elif op == '-':
                        stack.append(-1 * cur)
                    elif op == '*':
                        stack.append(stack.pop() * cur)
                    op = e

            total = 0
            while stack:
                total += stack.pop()
            return total
                
        
        def addOperatorsRecursive(i, expression):
            if i == len(num):
                ret = evaluate(expression)
                if ret == target:
                    res.append("".join(expression))
                return
            
            for j in range(i, len(num)):
                integer = num[i:j+1]
                if integer[0] == '0' and len(integer) > 1: # imp to not create numbers with 0 as prefix
                    return

                expression.append(integer)
                if j == len(num)-1:
                    addOperatorsRecursive(j+1, expression)
                else:
                    for op in operators:
                        expression.append(op)
                        addOperatorsRecursive(j+1, expression)
                        expression.pop()
                expression.pop()

        addOperatorsRecursive(0, [])
        return res


sol = Solution()
print(sol.addOperators("123", 6))
print(sol.addOperators("123", 123))
print(sol.addOperators("6", 6))
print(sol.addOperators("232", 8))
print(sol.addOperators("105", 5))
print(sol.addOperators("00", 0))
print(sol.addOperators("3456237490", 9191))
print(sol.addOperators("123456789", 45)) # failed testcase
