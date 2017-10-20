"""
46. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

https://leetcode.com/problems/permutations/discuss/
Has a template for all such problems
But my solution below has a similar one but not the same
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def permute_recr(i, l):
            if i == l:
                copy = nums[:]
                result.append(copy)
                return
            for j in range(i, l):
                if i == j or (j > 0 and nums[i] != nums[j] and nums[j] != nums[j-1]):
                    swap(i, j)
                    permute_recr(i + 1, l)
                    swap(i, j)

        permute_recr(0, len(nums))

        return result

sol = Solution()
print(sol.permuteUnique([1,2,2,1]))
print(sol.permuteUnique([1,2,1,1]))
