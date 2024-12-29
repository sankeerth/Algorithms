"""
852. Peak Index in a Mountain Array

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.
Your task is to solve it in O(log(n)) time complexity.

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Constraints:
3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = lo + (hi-lo) // 2
            if arr[mid] < arr[mid+1]:
                lo = mid+1
            else:
                hi = mid

        return lo


sol = Solution()
print(sol.peakIndexInMountainArray([0,1,0]))
print(sol.peakIndexInMountainArray([0,2,1,0]))
print(sol.peakIndexInMountainArray([0,10,5,2]))
print(sol.peakIndexInMountainArray([0,10,15,4]))
