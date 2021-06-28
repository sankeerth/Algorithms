"""
241. Different Ways to Add Parentheses

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways 
to group numbers and operators. You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'
"""
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
        
        def diffWaysToComputeRecursive(expression):
            if expression in memo:
                return memo[expression]
            
            res = []
            if expression.isdigit():
                memo[expression] = [int(expression)]
                return memo[expression]
            
            for i, e in enumerate(expression):
                if e in ['+', '-', '*']:
                    left = diffWaysToComputeRecursive(expression[:i])
                    right = diffWaysToComputeRecursive(expression[i+1:])
                    for num1 in left:
                        for num2 in right:
                            ret = compute(num1, num2, e)
                            res.append(ret)
            memo[expression] = res
            return res

        return diffWaysToComputeRecursive(expression)


sol = Solution()
print(sol.diffWaysToCompute("3-4*5"))
print(sol.diffWaysToCompute("2*3-4*5"))
