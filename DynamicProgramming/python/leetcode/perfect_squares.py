"""
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
    1 <= n <= 10^4
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * 10000
        dp[0], dp[1], dp[4], dp[9] = 0, 1, 1, 1

        for i in range(2, n+1):
            limit = int(i ** .5)
            for j in range(limit, 0, -1):
                k = j * j
                dp[i] = min(dp[i], dp[i - k] + 1)

        return dp[n]


s = Solution()
print(s.numSquares(35))
print(s.numSquares(16))
print(s.numSquares(18))
print(s.numSquares(8405))
print(s.numSquares(8505))


"""
Recursive solution:

class Solution:
    def numSquares(self, n: int) -> int:
        memo = [-1] * 10000
        memo[0], memo[1], memo[4], memo[9] = 0, 1, 1, 1
        
        def numSquaresRecursive(n):
            if memo[n] != -1:
                return memo[n]
            res = n
            limit = int(n ** .5)
            for i in range(limit, 0, -1):
                temp = numSquaresRecursive(n - i*i) + 1
                res = min(res, temp)

            memo[n] = res
            return res

        return numSquaresRecursive(n)
"""
