"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMax, curMin = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            tempMax = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, curMin * num, tempMax * num)

            res = max(res, curMax)

        return res


sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))
print(sol.maxProduct([-2, 0, 1]))
print(sol.maxProduct([-2, 0, -1]))
print(sol.maxProduct([-4, -3, -2]))
