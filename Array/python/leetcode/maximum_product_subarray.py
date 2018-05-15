"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_prod, min_prod, result = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            temp = max_prod
            cur = nums[i]
            max_prod = max(max(max_prod * cur, cur), min_prod * cur)
            min_prod = min(min(min_prod * cur, cur), temp * cur)
            result = max(result, max_prod)

        return result


sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))
print(sol.maxProduct([-2, 0, 1]))
print(sol.maxProduct([-2, 0, -1]))
