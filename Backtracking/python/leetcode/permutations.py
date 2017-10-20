"""
46. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
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
                swap(i, j)
                permute_recr(i + 1, l)
                swap(i, j)

        permute_recr(0, len(nums))
        print(result)

sol = Solution()
sol.permute([1,2,1])
sol.permute([1,2,3])
