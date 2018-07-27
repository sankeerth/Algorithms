"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2

        def find_median(nums1, nums2):
            if len(nums1) + len(nums2) <= 4:
                return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) / 2

            mid1, mid2 = (len(nums1)-1) // 2, (len(nums2)-1) // 2
            if nums1[mid1] > nums2[mid2]:
                return find_median(nums1[:len(nums1)-mid2], nums2[mid2:])  # (nums1[:mid1+1], nums2[mid2+1:]) does not work for odd lengths
            else:
                return find_median(nums1[mid1:], nums2[:len(nums2)-mid1])  # (nums1[mid1+1:], nums2[:mid2+1]) does not work for odd lengths

        return find_median(nums1, nums2)


sol = Solution()
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
print(sol.findMedianSortedArrays([3, 4], [1, 2]))
print(sol.findMedianSortedArrays([1, 7], [5, 6]))
print(sol.findMedianSortedArrays([1, 6], [5, 7]))
print(sol.findMedianSortedArrays([1, 5, 6], [4, 8, 11]))
print(sol.findMedianSortedArrays([1, 3, 4, 8], [2, 5, 6, 7]))
print(sol.findMedianSortedArrays([1, 5, 6, 7], [2, 3, 4, 8]))
print(sol.findMedianSortedArrays([1, 5, 6, 7, 9], [2, 3, 4, 8, 11]))


'''
My solution for two arrays of same length arrays:

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2

        def find_median(nums1, nums2):
            if len(nums1) + len(nums2) <= 4:
                return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) / 2

            mid1, mid2 = (len(nums1)-1) // 2, (len(nums2)-1) // 2
            if nums1[mid1] > nums2[mid2]:
                return find_median(nums1[:len(nums1)-mid2], nums2[mid2:])  # (nums1[:mid1+1], nums2[mid2+1:]) does not work for odd lengths
            else:
                return find_median(nums1[mid1:], nums2[:len(nums2)-mid1])  # (nums1[mid1+1:], nums2[:mid2+1]) does not work for odd lengths

        return find_median(nums1, nums2)
'''
