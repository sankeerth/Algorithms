"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i, j = 0, 0
        result = float('inf')
        current_sum = 0

        while j < len(nums):
            current_sum += nums[j]
            while i <= j and current_sum >= s:
                if j - i + 1 < result:
                    result = j - i + 1
                current_sum -= nums[i]
                i += 1
            j += 1

        return result if result != float('inf') else 0


sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(0, [2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(2, [1, 1, 3, 1, 1]))
