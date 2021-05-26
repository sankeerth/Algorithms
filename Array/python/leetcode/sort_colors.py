"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so 
that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""
from typing import List


class Solution:
    """
    Let's use here three pointers to track the rightmost boundary of zeros, the leftmost boundary of twos 
    and the current element under the consideration.

    Algorithm

    Initialize the rightmost boundary of zeros : p0 = 0. During the algorithm execution nums[idx < p0] = 0.
    Initialize the leftmost boundary of twos : p2 = n - 1. During the algorithm execution nums[idx > p2] = 2.
    Initialize the index of current element to consider : curr = 0.

    While curr <= p2 :
        If nums[curr] = 0 : swap curr and p0th elements and move both pointers to the right.
        If nums[curr] = 2 : swap curr and p2th elements. Move pointer p2 to the left.
        If nums[curr] = 1 : move pointer curr to the right.
    """
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while white <= blue:
            if nums[white] == 0:
                swap(red, white)
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                swap(white, blue)
                blue -= 1

        return nums



sol = Solution()
print(sol.sortColors([2,2,0,0,1,1]))
print(sol.sortColors([1,1,1,0,0,2,1]))
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


"""
My accepted solution:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
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
"""
