"""
154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1

        return nums[lo]


sol = Solution()
print(sol.findMin([1,3,5]))
print(sol.findMin([2,2,2,0,1]))
print(sol.findMin([2,2,2,0,2]))
print(sol.findMin([2,0,2,2,2]))
print(sol.findMin([2,2,2,2,2,2,2,0,1,1,2,2]))
print(sol.findMin([2,2,0,1,1,2,2,2,2,2,2,2]))


"""
My solution:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                while lo < mid and nums[lo] == nums[mid]:
                    lo += 1
                while hi > mid and nums[hi] == nums[mid]:
                    hi -= 1

                mid = (lo + hi) // 2
                if nums[mid] > nums[mid+1]:
                    return mid+1

                if nums[mid] <= nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo


        index = binarySearch(0, len(nums)-1)
        return nums[index]
"""
