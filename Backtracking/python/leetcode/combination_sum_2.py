"""
40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort(reverse=True)
        current = list()
        result = list()

        def combination_sum2_recr(i, l, total):
            if total == target:
                result.append(list(current))
            else:
                for j in range(i, l):
                    if i == j or candidates[j] + total <= target and candidates[j] != candidates[j-1]:
                        total += candidates[j]
                        current.append(candidates[j])
                        combination_sum2_recr(j+1, l, total)
                        current.pop()
                        total -= candidates[j]

        combination_sum2_recr(0, len(candidates), 0)

        return result

sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 29))
