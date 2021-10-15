"""
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it 
represented by an array nums. You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10

Constraints:
n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # reframe the problem
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in range(len(nums))]

        def maxCoinsRecursive(left, right):
            # no more balloons can be added
            if left + 1 == right:
                return 0

            # we've already seen this, return from cache
            if dp[left][right]:
                return dp[left][right]

            res = 0
            # add each balloon on the interval and return the maximum score
            for i in range(left+1, right):
                cur = nums[left] * nums[i] * nums[right]
                l = maxCoinsRecursive(left, i)
                r = maxCoinsRecursive(i, right)
                res = max(res, cur+l+r)
            dp[left][right] = res
            return res

        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return maxCoinsRecursive(0, len(nums)-1)


sol = Solution()
print(sol.maxCoins([3,5,8]))
print(sol.maxCoins([3,1,5,8]))
print(sol.maxCoins([3,1,5,8,5,7,10,21,6,15]))
print(sol.maxCoins([3,1,5,8,5,7,10,21,6,15,8,21,67,80,12]))
#print(sol.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]))

"""
My optimized solution:

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def maxCoinsRecursive(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return nums[0] * nums[1] + max(nums[0], nums[1])
            res = 0
            s = str(nums)
            if s in memo:
                return memo[s]
            
            for i in range(len(nums)):
                left = nums[i-1] if i > 0 else 1
                right = nums[i+1] if i < len(nums)-1 else 1
                product = left * nums[i] * right
                sumOfProducts = product + maxCoinsRecursive(nums[0:i] + nums[i+1:])
                res = max(res, sumOfProducts)
            
            memo[s] = res
            return res

        return maxCoinsRecursive(nums)
"""
