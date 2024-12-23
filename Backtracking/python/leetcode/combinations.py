"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List

# Backtracking skeleton (Good explanation in Leetocode Editorial)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def recursive(i, arr):
            if len(arr) == k:
                res.append(list(arr))
                return
            for j in range(i, n+1):
                arr.append(j)
                recursive(j+1, arr)
                arr.pop()

        recursive(1, [])

        return res


sol = Solution()
print(sol.combine(4, 2))
print(sol.combine(4, 0))
print(sol.combine(3, 1))
print(sol.combine(3, 3))


"""
My other solution:
To include or not include the number.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def recursive(i, arr):
            if i > n or len(arr) + n - i + 1 < k:
                return
            if len(arr) == k:
                res.append(list(arr))
                return
            
            recursive(i+1, arr + [i+1])
            recursive(i+1, arr)

        recursive(0, [])

        return res
"""
