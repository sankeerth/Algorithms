"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no 
elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up:
Could you come up with the O(n2) solution?
Could you improve it to O(n log(n)) time complexity?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(res, dp[i])

        return res


sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))
print(sol.lengthOfLIS([7,7,7,7,7,7,7]))


"""
Recursive solution:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        memo[len(nums)-1] = 1

        def lengthOfLISRecursive(i):
            if i == len(nums)-1:
                return 1
            
            if memo[i] != -1:
                return memo[i]
            
            for j in range(i+1, len(nums)):
                res = lengthOfLISRecursive(j)
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + res)
            memo[i] = max(1, memo[i])
            return memo[i]

        lengthOfLISRecursive(0)
        return max(memo)
"""
