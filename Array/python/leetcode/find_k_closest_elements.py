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


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def binary_search(lo, hi, target):
            """
            binary search to find the closest index to the target
            this is not used in the solution below. this function is there for reference
            :param lo:
            :param hi:
            :param target:
            :return:
            """
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target < arr[mid+1]:
                    return mid if abs(target - arr[mid]) <= abs(arr[mid+1] - target) else mid+1
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

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
