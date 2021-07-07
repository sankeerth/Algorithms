"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        rNum1 = num1[::-1]
        rNum2 = num2[::-1]
        
        n = max(len(num1), len(num2))
        carry = 0
        for i in range(n):
            c1 = 0 if i >= len(rNum1) else int(rNum1[i])
            c2 = 0 if i >= len(rNum2) else int(rNum2[i])

            s = (c1 + c2 + carry) % 10
            carry = (c1 + c2 + carry) // 10
            res.append(str(s))
        
        if carry > 0:
            res.append(str(carry))
            
        return "".join(res[::-1])


sol = Solution()
print(sol.addStrings("11", "123"))
print(sol.addStrings("456", "77"))
print(sol.addStrings("0", "0"))
print(sol.addStrings("999", "1"))
print(sol.addStrings("999", "111"))
