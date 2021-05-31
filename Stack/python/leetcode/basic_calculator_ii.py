"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        operandStack, operatorStack = [], []
        precedence = {'+': 0, '-': 0, '*': 1, '/': 1}

        def performOperation(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return int(a / b)
            else:
                pass # can add exception handling for invalid operator

        def calculate():
            b = operandStack.pop()
            a = operandStack.pop()
            op = operatorStack.pop()

            res = performOperation(a, b, op)
            operandStack.append(res)

        num = ""
        for c in s:
            if c in ['+', '-', '*', '/']:
                operandStack.append(int(num))
                num = ""
                while operatorStack and precedence[c] <= precedence[operatorStack[-1]]:
                    # can have exception handling to ensure there are at least 2 operands in operand stack
                    calculate()
                operatorStack.append(c)
            else:
                num += c
        
        # exception handling to ensure num is not empty string as the expression must end with a number
        operandStack.append(int(num))

        while operatorStack:
            calculate()

        res = operandStack[0]
        return res


sol = Solution()
print(sol.calculate("3+2*2"))
print(sol.calculate("3-2*2"))
print(sol.calculate(" 3/2 "))
print(sol.calculate(" 3+5 / 2 "))
print(sol.calculate(" 5 / 2+3 "))
print(sol.calculate(" 7 * 5/2"))
print(sol.calculate("5/2 *3"))
print(sol.calculate("3+5-4*3"))
print(sol.calculate("1*2-3/4+5*6"))


"""
Leetcode solution:
Approach 1: Using Stack (Uses one stack for numbers instead of two like I did)


If the current operation is addition (+) or subtraction (-), then the expression is evaluated based on 
the precedence of the next operation. Ex: '4+3*5'

If the current operator is multiplication (*) or division (/), then the expression is evaluated irrespective of 
the next operation. This is because in the given set of operations (+,-,*,/), the * and / operations have the 
highest precedence and therefore must be evaluated first. Ex: '4*3+5'

Algorithm

Scan the input string s from left to right and evaluate the expressions based on the following rules
If the current character is a digit 0-9 ( operand ), add it to the number currentNumber.
Otherwise, the current character must be an operation (+,-,*, /). Evaluate the expression based on the type of operation.
Addition (+) or Subtraction (-): We must evaluate the expression later based on the next operation. 
So, we must store the currentNumber to be used later. Let's push the currentNumber in the Stack.
Multiplication (*) or Division (/): Pop the top values from the stack and evaluate the current expression. 
Push the evaluated value back to the stack.

class Solution {
    public int calculate(String s) {

        if (s == null || s.isEmpty()) return 0;
        int len = s.length();
        Stack<Integer> stack = new Stack<Integer>();
        int currentNumber = 0;
        char operation = '+';
        for (int i = 0; i < len; i++) {
            char currentChar = s.charAt(i);
            if (Character.isDigit(currentChar)) {
                currentNumber = (currentNumber * 10) + (currentChar - '0');
            }
            if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == len - 1) {
                if (operation == '-') {
                    stack.push(-currentNumber);
                }
                else if (operation == '+') {
                    stack.push(currentNumber);
                }
                else if (operation == '*') {
                    stack.push(stack.pop() * currentNumber);
                }
                else if (operation == '/') {
                    stack.push(stack.pop() / currentNumber);
                }
                operation = currentChar;
                currentNumber = 0;
            }
        }
        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }
        return result;
    }
}
"""

"""
Leetcode solution
Approach 2: Optimised Approach without the stack

We could add the values to the result beforehand and keep track of the last calculated number, thus eliminating the need for the stack.

Algorithm:
The approach works similar to Approach 1 with the following differences :
Instead of using a stack, we use a variable lastNumber to track the value of the last evaluated expression.
If the operation is Addition (+) or Subtraction (-), add the lastNumber to the result instead of pushing it to the stack. 
The currentNumber would be updated to lastNumber for the next iteration.
If the operation is Multiplication (*) or Division (/), we must evaluate the expression lastNumber * currentNumber and update 
the lastNumber with the result of the expression. This would be added to the result after the entire string is scanned.

class Solution:
    def calculate(self, s: str) -> int:
        lastNumber, currentNumber, res = 0, 0, 0
        operation = '+'

        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                currentNumber = (currentNumber * 10) + int(char)
            if char in ['+', '-', '*', '/'] or i == len(s)-1:
                if operation == '+' or operation == '-':
                    res += lastNumber
                    lastNumber = currentNumber if operation == '+' else -currentNumber
                elif operation == '*':
                    lastNumber = lastNumber * currentNumber
                elif operation == '/':
                    lastNumber = int(lastNumber / currentNumber)
                operation = char
                currentNumber = 0
            i += 1

        res += lastNumber
        return res
"""
