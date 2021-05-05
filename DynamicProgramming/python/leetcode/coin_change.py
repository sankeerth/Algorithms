"""
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return -1 if dp[amount] == float('inf') else dp[amount]


sol = Solution()
print(sol.coinChange([1,2,5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([3,5], 2))
print(sol.coinChange([1], 0))
print(sol.coinChange([1], 1))
print(sol.coinChange([1], 2))


"""
Recursive solution

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        for coin in coins:
            memo[coin] = 1

        def coinChangeRecursive(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            elif amount in memo:
                return memo[amount]
        
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + coinChangeRecursive(amount-coin))
            
            memo[amount] = res
            return res

        res = coinChangeRecursive(amount)
        return -1 if res == float('inf') else res
"""

"""
Time Complexity of Brute Force:

Time complexity : O(S^n). In the worst case, complexity is exponential in the number of the coins n.
The reason is that every coin denomination ci could have at most (S/ci) values. 
Therefore the number of possible combinations is:

(S/c1) * (S/c2) * (S/c3) ... = (S^n)/(c1*c2*c3...cn) => O(S^n)

Time Complexity of DP:

Time complexity : O(S*n), where S is the amount, n is denomination count. 
In the worst case the recursive tree of the algorithm has height of S and the algorithm solves 
only S subproblems because it caches precalculated solutions in a table. Each subproblem is computed with n iterations, 
one by coin denomination. Therefore there is O(S*n)O(S∗n) time complexity.
"""
