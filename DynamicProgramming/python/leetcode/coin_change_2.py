"""
518. Coin Change 2

You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot 
be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
0 <= amount <= 5000
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        minChange = min(coins)
        memo = {}
        if amount == 0:
            return 0

        def changeRecursive(amount):
            if amount == 0:
                return 1
            if amount < minChange:
                return 0
            if amount in memo:
                return memo[amount]

            res = 0
            for coin in coins:
                if amount-coin >= 0:
                    res += changeRecursive(amount-coin)

            memo[amount] = res
            return res

        return changeRecursive(amount)


sol = Solution()
# print(sol.change(11, [1,2,5]))
print(sol.change(5, [1,2,5]))
print(sol.change(3, [2]))
print(sol.change(2, [3,5]))
print(sol.change(0, [1]))
print(sol.change(1, [1]))
print(sol.change(2, [1]))
