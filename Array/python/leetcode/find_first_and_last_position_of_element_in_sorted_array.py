"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        first = binarySearch(0, len(nums)-1)
        queue = []
        if first != -1:
            queue = [first-1, first+1]
        leftIndex, rightIndex = first, first

        while queue:
            val = queue.pop(0)
            if val < first:
                left = binarySearch(0, val)
                if left != -1:
                    queue.append(left-1)
                    leftIndex = left
            else:
                right = binarySearch(val, len(nums)-1)
                if right != -1:
                    queue.append(right+1)
                    rightIndex = right

        return [leftIndex, rightIndex]


sol = Solution()
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 4))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 5))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 7))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 8))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 9))
print(sol.searchRange([4,5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10], 11))
