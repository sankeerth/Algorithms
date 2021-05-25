"""
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Constraints:
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i, j = 1, 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        print(nums)
        return j


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
print(sol.removeDuplicates([1,1,1,1,1,1,1]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


"""
My solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        i, j = 0, 0

        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j == len(nums): break
            i += 1
            swap(nums, i, j)
            j += 1

        return i+1
"""
