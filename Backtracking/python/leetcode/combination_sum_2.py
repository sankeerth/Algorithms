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

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, cur = [], []
        candidates.sort(reverse=True)

        def combinationSum2Recursive(i, total):
            if total == target:
                res.append(list(cur))
            else:
                for j in range(i, len(candidates)):
                    if i == j or candidates[j] != candidates[j-1]:
                        if candidates[j] + total <= target:
                            cur.append(candidates[j])
                            combinationSum2Recursive(j+1, total + candidates[j])
                            cur.pop()

        combinationSum2Recursive(0, 0)
        return res


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 29))
