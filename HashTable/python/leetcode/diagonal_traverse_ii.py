"""
1424. Diagonal Traverse II

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Constraints:
1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(deque) # defaultdict(list)
        maxIndex = 0
        res = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                maxIndex = max(maxIndex, i+j)
                diagonals[i+j].appendleft(nums[i][j]) # append(nums[i][j])

        for i in range(maxIndex+1):
            res += diagonals[i] # [::-1]

        return res


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,4,2,7,5,3,8,6,9]
print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])) # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
