"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
import random


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def partition(lo, hi):
            i, j = lo+1, hi
            pivot = nums[lo]

            while True:  # careful here if [4,5] | lo=0, hi=1, i=1, j=1  if it was 'while i<j', swap(lo, j) => [5,4]
                while nums[i] <= pivot and i < hi:  # careful here, missing i < hi would result it index out of bound
                    i += 1

                while nums[j] >= pivot and j > lo:  # careful here, missing j > lo would end up swapping wrong number
                    j -= 1

                if i >= j:
                    break

                swap(i, j)

            swap(lo, j)
            return j

        lo, hi = 0, len(nums)-1
        k = len(nums) - k
        random.shuffle(nums)

        while lo < hi:
            index = partition(lo, hi)
            if index < k:
                lo = index + 1
            elif index > k:
                hi = index - 1
            else:
                break

        return nums[k]


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 4, 6, 5], 2))
print(sol.findKthLargest([1, 1, 1, 1, 2], 2))
print(sol.findKthLargest([1, 1, 1, 1, 2], 1))
print(sol.findKthLargest([1, 0, 0, 1, 0, 1, 0], 4))
