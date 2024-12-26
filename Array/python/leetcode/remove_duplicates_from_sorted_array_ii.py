"""
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of 
nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
Explanation: Your function should return length = 7, with the first seven elements of nums being 
modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.

Constraints:
    1 <= nums.length <= 3 * 104
    -104 <= nums[i] <= 104
    nums is sorted in ascending order.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, count = 1, 1, 1
        k = 2

        while i < len(nums):
            if nums[i] != nums[i-1] or count < k:
                if nums[i] != nums[i-1]:
                    count = 0
                nums[j] = nums[i]
                j += 1

            count += 1
            i += 1

        print(nums)
        return j


sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(sol.removeDuplicates([1,1,1,2,2,3]))


"""
Leetcode solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        count = 1

        while j < len(nums):
            if nums[j] == nums[j-1]:
                count += 1
                if count > 2:
                    j += 1
                    continue
            else:
                count = 1
            nums[i] = nums[j]
            i += 1
            j += 1

        return i
"""
