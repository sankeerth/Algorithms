"""
81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            while lo < mid and nums[lo] == nums[mid]:  # to take care of [2, 0, 2, 2, 2], 0
                lo += 1
            if nums[lo] <= nums[mid]:  # left half is sorted
                if nums[lo] <= target < nums[mid]:  # target is in the first half
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right half is sorted
                if nums[mid] < target <= nums[hi]:  # target is in the second half
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False


sol = Solution()
print(sol.search([2, 5, 6, 0, 0, 1, 2], 0))
print(sol.search([2, 5, 6, 0, 0, 1, 2], 3))
print(sol.search([2, 2, 2, 0, 1], 0))
print(sol.search([2, 2, 2, 0, 1], 3))
print(sol.search([2, 2, 2, 0, 2], 0))
print(sol.search([2, 0, 2, 2, 2], 0))
print(sol.search([2, 0, 2, 2, 2], 3))
