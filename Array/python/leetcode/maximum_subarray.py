"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23 

Constraints:
1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum, max_sum = 0, nums[0]

        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


"""
Another variant:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, prevSum = nums[0], 0
        for num in nums:
            curSum = max(prevSum + num, num)
            prevSum = max(0, curSum)
            res = max(res, curSum)

        return res
"""
