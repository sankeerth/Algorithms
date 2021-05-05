"""
673. Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing. 

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:
1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
from typing import List


class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        dp, count, longest = [1] * len(nums), [1] * len(nums), 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
            longest = max(longest, dp[i])

        res = 0
        for i in range(len(count)):
            if dp[i] == longest:
                res += count[i]

        return res


sol = Solution()
print(sol.findNumberOfLIS([7,9,4,10,5,6]))
print(sol.findNumberOfLIS([1,3,5,4,7]))
print(sol.findNumberOfLIS([1,3,6,5,4,7]))
print(sol.findNumberOfLIS([2,2,2,2,2]))


"""
Solution using backward approach where f(0) is solved before f(1)

class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        dp, count, longest = [1] * len(nums), [1] * len(nums), 1

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            longest = max(longest, dp[i])

        return sum(c for i, c in enumerate(count) if dp[i] == longest)
"""
