"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]

        return res


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))
print(sol.productExceptSelf([-2,1,-3,4,-1,2,1,-5,4]))


"""
Solution with O(n) complexity and O(n) space:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, prodFromLeft, prodFromRight = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        prodFromLeft[0], prodFromRight[-1] = nums[0], nums[-1]
        l = len(nums)

        for i in range(1, l):
            prodFromLeft[i] = nums[i] * prodFromLeft[i-1]
        for i in range(l-2, -1, -1):
            prodFromRight[i] = nums[i] * prodFromRight[i+1]

        res[0], res[-1] = prodFromRight[1], prodFromLeft[l-2]
        for i in range(1, l-1):
            res[i] = prodFromLeft[i-1] * prodFromRight[i+1]

        return res
"""
