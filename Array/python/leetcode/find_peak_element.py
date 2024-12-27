"""
162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


class Solution:
"""
We can view any given sequence in nums array as alternating ascending and descending sequences. By making use of this, and the fact that we can return any peak as the result, 
we can make use of Binary Search to find the required peak element.

In case of simple Binary Search, we work on a sorted sequence of numbers and try to find out the required number by reducing the search space at every step. 
In this case, we use a modification of this simple Binary Search to our advantage. We start off by finding the middle element, mid from the given nums array. 
If this element happens to be lying in a descending sequence of numbers. or a local falling slope(found by comparing nums[i] to its right neighbour), 
it means that the peak will always lie towards the left of this element. Thus, we reduce the search space to the left of mid(including itself) and perform the same process on left subarray.

If the middle element, mid lies in an ascending sequence of numbers, or a rising slope(found by comparing nums[i] to its right neighbour), it obviously implies that the peak lies towards the right of this element. 
Thus, we reduce the search space to the right of mid and perform the same process on the right subarray.

In this way, we keep on reducing the search space till we eventually reach a state where only one element is remaining in the search space. This single element is the peak element.
"""
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid+1]:
                lo = mid+1
            else:
                hi = mid-1

        return lo


sol = Solution()
print(sol.findPeakElement([1,2,3,1]))
print(sol.findPeakElement([1,2,1,3,5,6,4]))
print(sol.findPeakElement([3,4,3,2,1]))
