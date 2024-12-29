"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


# My rudimentary solution with O(M * (M+N)) time
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        intermediate, res = [], []

        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        def mulWithSingleDigit(a, num, zeros):
            total, carry = [], 0

            for _ in range(zeros):
                total.append(0)

            for n in num[::-1]:
                mul = (int(n) * int(a)) + carry
                unit = mul % 10
                carry = mul // 10
                total.append(unit)
            if carry > 0:
                total.append(carry)
            return total

        zeros = 0
        for a in num1[::-1]:
            total = mulWithSingleDigit(a, num2, zeros)
            intermediate.append(total)
            zeros += 1

        maxlen = max(len(l) for l in intermediate)

        carry = 0
        for j in range(maxlen):
            total = 0
            for i in range(len(intermediate)):
                if j < len(intermediate[i]):
                    total += intermediate[i][j] 
            
            total += carry
            digit = total % 10
            carry = total // 10

            res.append(digit)
        
        if carry > 0:
            res.append(carry)

        res = [str(c) for c in res[::-1]]
        return "".join(res)


sol = Solution()
print(sol.multiply("123", "456"))
print(sol.multiply("12", "0"))
print(sol.multiply("45656843", "223"))


"""
Leetcode solution: O(M*N)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                zeros = i+j
                carry = res[zeros]
                mul = int(d1) * int(d2) + carry
                
                digit = mul % 10
                carry = mul // 10

                res[zeros] = digit
                res[zeros+1] += carry

        if res[-1] == 0:
            res.pop()
        
        res = [str(d) for d in res[::-1]]
        return "".join(res)
"""
