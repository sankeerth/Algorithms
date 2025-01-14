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
            nums[i], nums[j] = nums[j], nums[i]
        
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


"""
First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.
For example, no next permutation is possible for the following array:

[9, 5, 4, 3, 1]
We need to find the first pair of two successive numbers a[i] and a[i−1], from the right, which satisfy
a[i]>a[i−1]. Now, no rearrangements to the right of a[i−1] can create a larger permutation since that subarray consists of numbers in descending order.
Thus, we need to rearrange the numbers to the right of a[i−1] including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. 
Therefore, we need to replace the number a[i−1] with the number which is just larger than itself among the numbers lying to its right section, say a[j].

Next Permutation 

We swap the numbers a[i−1] and a[j]. We now have the correct number at index i−1. But still the current permutation isn't the permutation
that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of a[i−1]. Therefore, we need to place those
numbers in ascending order to get their smallest permutation.

But, recall that while scanning the numbers from the right, we simply kept decrementing the index
until we found the pair a[i] and a[i−1] where, a[i]>a[i−1]. Thus, all numbers to the right of a[i−1] were already sorted in descending order.
Furthermore, swapping a[i−1] and a[j] didn't change that order.
Therefore, we simply need to reverse the numbers following a[i−1] to get the next smallest lexicographic permutation.
"""
