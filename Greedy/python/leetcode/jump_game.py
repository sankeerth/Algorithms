"""
55. Jump Game

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
    1 <= nums.length <= 3 * 104
    0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    # Read good explanation solution section for backtracking, DP and Greedy approaches
    # scan from end
    def canJump(self, nums: List[int]) -> bool:
        leftMostIndexLeadingToLastIndex = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= leftMostIndexLeadingToLastIndex:
                leftMostIndexLeadingToLastIndex = i
            
        return leftMostIndexLeadingToLastIndex == 0

    # scan from start
    def canJump(self, nums: List[int]) -> bool:
            i, jump, n = 0, 0, len(nums)
    
            while i <= jump and i < n:
                jump = max(jump, i+nums[i])
                i += 1
            
            return jump >= n-1


sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
print(sol.canJump([1,5,2,1,0,2,0]))
print(sol.canJump([5,4,3,2,1,0,0]))
print(sol.canJump([2,4,2,1,0,2,0]))
print(sol.canJump([9,4,2,1,0,2,0]))


"""
Backtracking solution O(2^n):

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpRecursive(index):
            if index == len(nums)-1:
                return True

            farthest = min(index + nums[index], len(nums)-1)
            for i in range(index+1, farthest+1):
                if canJumpRecursive(i):
                    return True
            return False

        return canJumpRecursive(0)
"""

"""
Memoization (top-down) solution O(n^2):

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        memo[-1] = True

        def canJumpRecursive(index):
            if memo[index] != -1:
                return memo[index]

            farthest = min(index + nums[index], len(nums)-1)
            for i in range(farthest, index, -1): # optimization to start from farthest instead of next index
                if canJumpRecursive(i):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False

        return canJumpRecursive(0)
"""

"""
DP (bottom-up) solution O(n^2):

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        memo[-1] = True

        for i in range(len(nums)-2, -1, -1):
            farthest = min(i + nums[i], len(nums)-1)
            for j in range(farthest, i, -1):
                if memo[j]:
                    memo[i] = True
                    break
        
        return memo[0]
"""
