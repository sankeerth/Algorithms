"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted 
in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def firstDecreaseFromRight():
            i = len(nums)-2
            while i >= 0:
                if nums[i] < nums[i+1]:
                    return i
                i -= 1
            return i
        
        def firstGreaterThanLeftSwap(leftSwap):
            i = len(nums)-1
            while i > leftSwap:
                if nums[i] > nums[leftSwap]:
                    return i
                i -= 1
            return -1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        def reverse(i, j):
            while i < j:
                swap(i, j)
                i += 1
                j -= 1

        leftSwap = firstDecreaseFromRight()
        if leftSwap < 0:
            reverse(0, len(nums)-1)
            return nums

        rightSwap = firstGreaterThanLeftSwap(leftSwap)
        swap(leftSwap, rightSwap)

        reverse(leftSwap+1, len(nums)-1)
        return nums


sol = Solution()
print(sol.nextPermutation([1,2,3]))
print(sol.nextPermutation([3,2,1]))
print(sol.nextPermutation([1,1,5]))
print(sol.nextPermutation([1,3,2]))

