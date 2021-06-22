"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


class Solution:
    # O(log n) time and O(1) space
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647 # 2**31 - 1
        MIN_INT = -2147483648 # -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives, quotient = 2, 0
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        highestPowerOfTwo, count = divisor, 1
        while dividend - highestPowerOfTwo <= 0:
            highestPowerOfTwo = highestPowerOfTwo << 1
            count = count << 1
            
        while dividend - divisor <= 0:
            if dividend - highestPowerOfTwo <= 0:
                dividend -= highestPowerOfTwo
                quotient += count

            highestPowerOfTwo = highestPowerOfTwo >> 1
            count = count >> 1

        return -quotient if negatives == 1 else quotient


sol = Solution()
print(sol.divide(3, -1))
print(sol.divide(-24, -4))
print(sol.divide(694, 53))
print(sol.divide(93706, 157))
print(sol.divide(-10388934, 134))
print(sol.divide(1979384243, 478))


"""
O(n) time with O(1) space

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647 # 2**31 - 1
        MIN_INT = -2147483648 # -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives, quotient = 2, 0
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        while dividend - divisor <= 0:
            dividend -= divisor
            quotient += 1

        return -quotient if negatives == 1 else quotient
"""

"""
O(log n) time with O(log n) space

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647 # 2**31 - 1
        MIN_INT = -2147483648 # -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives, quotient = 2, 0
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        dividendCopy, divisorCopy = dividend, divisor
        divisorIntoPowerOfTwos = []
        while dividendCopy - divisorCopy <= 0:
            divisorIntoPowerOfTwos.append(divisorCopy)
            divisorCopy += divisorCopy

        for i in range(len(divisorIntoPowerOfTwos)-1, -1, -1):
            if dividend <= divisorIntoPowerOfTwos[i]:
                quotient += 2 ** i
                dividend -= divisorIntoPowerOfTwos[i]

        # while dividend - divisor <= 0:
        #     val = divisorIntoPowerOfTwos.pop()
        #     if dividend - val <= 0:
        #         quotient += 2 ** len(divisorIntoPowerOfTwos)
        #         dividend -= val

        return -quotient if negatives == 1 else quotient
"""
