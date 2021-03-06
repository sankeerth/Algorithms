"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

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
        res, cur = [], []
        candidates.sort(reverse=True)

        def combinationSumRecursive(i, total):
            if total == target:
                res.append(list(cur))
            else:
                for j in range(i, len(candidates)):
                    if candidates[j] + total <= target:
                        cur.append(candidates[j])
                        combinationSumRecursive(j, total + candidates[j])
                        cur.pop()

        combinationSumRecursive(0, 0)
        return res


sol = Solution()
print(sol.combinationSum([2,7,3,6], 7))
print(sol.combinationSum([2,7,3,1], 14))
