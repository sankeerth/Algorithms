"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse=True)
        result = list()
        current = list()

        def combination_sum_recr(i, l, total):
            if total == target:
                result.append(list(current))
                return
            for j in range(i, l):
                if candidates[j] + total <= target:
                    current.append(candidates[j])
                    total += candidates[j]
                    combination_sum_recr(j, l, total)
                    current.pop()
                    total -= candidates[j]

        combination_sum_recr(0, len(candidates), 0)

        return result

sol = Solution()
print(sol.combinationSum([2,7,3,1], 14))
