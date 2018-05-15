"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        current_sum, max_sum = 0, nums[0]

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
