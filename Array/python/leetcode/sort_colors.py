"""
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i, j, l = 0, len(nums) - 1, len(nums)

        def swap(i, j, nums):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while True:
            while i < j:
                if nums[i] > nums[j]:
                    swap(i, j, nums)
                j -= 1

            while i < l - 1 and nums[i + 1] == nums[i]:
                i += 1

            if i < l - 1:
                i += 1

            if i == l - 1:
                break
            else:
                j = l - 1

        return nums

sol = Solution()
print(sol.sortColors([0,1,2,1,2]))
print(sol.sortColors([0,1,2,1,2,0]))
print(sol.sortColors([0,1,1,0,2,2,1,0,2,1]))
print(sol.sortColors([1,1,1,0,0,0,2,2]))
print(sol.sortColors([0,0,0,1,1,2,2,2]))
print(sol.sortColors([2,2,0,0,1,1]))
print(sol.sortColors([2,2,1,1,0,0]))
print(sol.sortColors([0,0,1,1,2,2]))
print(sol.sortColors([1,1,0,0,2,2]))
print(sol.sortColors([1,1,2,2,0,0]))