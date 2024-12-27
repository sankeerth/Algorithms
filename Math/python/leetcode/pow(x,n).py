"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            res = 1
            while n > 0:
                if n % 2 == 1:
                    res = res * x
                    n -= 1
                x = x * x
                n = n // 2
            return res

        val = pow(x, abs(n))
        return val if n >= 0 else 1/val


sol = Solution()
print(sol.myPow(2.0, 10))
print(sol.myPow(2.1, 3))
print(sol.myPow(2.0, -2))
print(sol.myPow(2.0, -200000000))
print(sol.myPow(0.00001, 2147483647))
print(sol.myPow(0.44528, 0))


"""
Iterarive solution:

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            res = 1
            while n > 0:
                if n % 2 == 1:
                    res = res * x
                    n -= 1
                x = x * x
                n = n // 2
            return res

        val = pow(x, abs(n))
        return val if n >= 0 else 1/val
"""
