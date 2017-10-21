"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = list()
        current = list()
        nums.sort()

        def subsets_recr(i, l):
            result.append(list(current))
            for j in range(i, l):
                if i == j or nums[j] != nums[j-1]:
                    current.append(nums[j])
                    subsets_recr(j+1, l)
                    current.pop()

        subsets_recr(0, len(nums))

        return result

sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
print(sol.subsetsWithDup([1, 1, 2, 2]))
