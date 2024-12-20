"""
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permutations(arr, counter):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    arr.append(num)
                    permutations(arr, counter)
                    arr.pop()
                    counter[num] += 1
        
        permutations([], Counter(nums))
        return res


sol = Solution()
print(sol.permuteUnique([1,2,2,1]))
print(sol.permuteUnique([1,2,1,1]))
print(sol.permuteUnique([1,2,3]))


"""
Template for such problems: https://leetcode.com/problems/permutations/discuss/
"""
