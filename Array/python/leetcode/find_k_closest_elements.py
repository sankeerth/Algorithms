"""
658. Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # leetcode solution which is simpler instead of using binary search to find the closest element
        # and keeping two pointers to move on either side until we get k closest elements
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Note it doesn't matter if we use abs or not
            # if abs(x - arr[mid]) > abs(arr[mid+k] - x):
            if (x - arr[mid]) > (arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


sol = Solution()
sol.findClosestElements([1, 2, 3, 4, 5], 4, 4)
sol.findClosestElements([1, 2, 3, 4, 5], 4, -1)

"""
My O(n) solution which is still accepted since worst case should be at least O(k) where k -> n (len of arr):

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [0] * len(arr)

        for i, num in enumerate(arr):
            diff[i] = abs(num - x)
        minimum = diff.index(min(diff))

        start, end = minimum, minimum
        while end - start + 1 < k:
            if start == 0:
                end += 1
            elif end == len(diff)-1:
                start -= 1
            elif diff[start-1] <= diff[end+1]:
                start -= 1
            elif diff[start-1] > diff[end+1]:
                end += 1

        return arr[start:end+1]
"""

"""
My binary search solution:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binarySearch(lo, hi, target):
            while lo <= hi:
                mid = (lo+hi) // 2
                if lo == hi:
                    return lo
                elif arr[mid] <= target <= arr[mid+1]:
                    return mid if abs(arr[mid]-target) <= abs(arr[mid+1]-target) else mid+1
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1 if mid - 1 > lo else lo # so that hi does not go less than lo to negative

        minimum = binarySearch(0, len(arr)-1, x)
        start, end = minimum, minimum

        while end - start + 1 < k:
            if start == 0:
                end += 1
            elif end == len(arr)-1:
                start -= 1
            elif abs(arr[start-1]-x) <= abs(arr[end+1]-x):
                start -= 1
            else:
                end += 1

        return arr[start:end+1]
"""
