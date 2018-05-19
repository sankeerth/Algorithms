"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        result = list()
        nums = sorted(nums)

        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                if l != i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue

                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
            i += 1

        return result


sol = Solution()
print(sol.threeSum([-1, -1, 2, 2, 0, 1, 2, -1, -4]))
print(sol.threeSum([-1, 1, 2]))
print(sol.threeSum([-1, 1, 0]))
print(sol.threeSum([-1, 1]))
print(sol.threeSum([0, 0, 0]))
print(sol.threeSum([0, 0, 1]))

"""
from collections import Counter

'''
problem with the hashmap implementation:
1. Increase in complexity as list cannot be added to set. Therefore it has be added as a string by sorting numbers (to
avoid duplicates) and then split to convert to list before returning
2. However, a major problem would be with the logic as the third number (-1* sum of other two) is checked in the hashmap
but that could possibly be one of the other two in iteration ex: 4, -2 needs another -2 for sum to become 0. But -2 can
be picked from the the same set of 4, -2. That way same number would be included twice and additional logic check needs
to be applied to overcome this.

Hashset and hashmap solution can still be implemented but it becomes a little complicated than two pointer soln:
All solutions: https://fizzbuzzed.com/top-interview-questions-1/#twopointer

'''
class Solution:
    def threeSum(self, nums):
        result = set()
        nums_dict = Counter(nums)

        for i in range(len(nums)):
            cur_l = nums[i]
            for j in range(i+1, len(nums)):
                cur = (cur_l + nums[j]) * -1
                if cur in nums_dict:
                    result.add(str(cur_l) + ':' + str(nums[j]) + ':' + str(cur))

        print(result)
        return result


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
"""
