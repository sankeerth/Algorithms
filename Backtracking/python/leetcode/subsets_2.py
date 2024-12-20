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
        result, current = [], []
        nums.sort()

        def subsets_recr(i):
            result.append(list(current))
            for j in range(i, len(nums)):
                if i == j or nums[j] != nums[j-1]:
                    current.append(nums[j])
                    subsets_recr(j+1)
                    current.pop()

        subsets_recr(0)
        return result


sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
print(sol.subsetsWithDup([1, 1, 2, 2]))


"""
Modification of 'Either include the digit or not'.

class Solution(object):
    def subsets(self, nums):
        res = []
        nums.sort()

        def subsetsRecursive(i, sub):
            if i == len(nums):
                res.append(sub)
                return

            subsetsRecursive(i+1, sub)
            # ignore individual repeated elements, for ex: [2] from [1, 2, 2, 2]
            if not sub and i > 0 and nums[i] == nums[i-1]:
                return
            # stop repeating subsets and taking it further, for ex: [1, 2] from [1, 2, 2, 2]
            if sub and nums[i] != sub[-1] and nums[i] == nums[i-1]:
                return
            subsetsRecursive(i+1, sub + [nums[i]])

        subsetsRecursive(0, [])
        return res
"""

"""
Iterative solution:

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        seen = set()
        nums.sort()

        for num in nums:
            for i in range(len(res)):
                sub = res[i] + [num]
                tup = tuple(sub)
                if tup not in seen:
                    res.append(sub)
                    seen.add(tup)
        
        return res
"""
