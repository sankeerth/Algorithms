"""
659. Split Array into Consecutive Subsequences

Given an array nums sorted in ascending order, return true if and only if you can 
split it into 1 or more subsequences such that each subsequence consists of 
consecutive integers and has length at least 3.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False

Constraints:
1 <= nums.length <= 10000
"""
from typing import List


# Same as my solution below, however, the length of each subsequence is stored 
# and not all the numbers in every subsequence. Just the last number of the subsequence
# and its length
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        i, consecutiveLength = 0, 3
        subsequences = []
        lengthOfSubsequences = []

        while i < len(nums):
            num = nums[i]
            end = len(subsequences)-1

            while end >= 0 and i < len(nums) and nums[i] == num:
                if subsequences[end][-1] == num-1:
                    subsequences[end].append(num)
                    subsequences[end].pop(0)
                    lengthOfSubsequences[end] += 1
                    i += 1
                end -= 1
            
            while i < len(nums) and nums[i] == num:
                subsequences.append([num])
                lengthOfSubsequences.append(1)
                i += 1

        for length in lengthOfSubsequences:
            if length < consecutiveLength:
                return False

        return True


s = Solution()
print(s.isPossible([1,2,3,3,4,5]))
print(s.isPossible([1,2,3,3,4,4,5,5]))
print(s.isPossible([1,2,3,4,4,5]))
print(s.isPossible([1,2,3,3,4,5,5,6,7]))
print(s.isPossible([1,2,3,4,4,5,6]))
print(s.isPossible([1,2]))
print(s.isPossible([1,2,2,2]))
print(s.isPossible([1,1,1,1]))


"""
Initial solution is not optimized since we have all the subsequences stored and not just the length

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        i, consecutiveLength = 0, 3
        subsequences = []

        while i < len(nums):
            num = nums[i]
            end = len(subsequences)-1

            while end >= 0 and i < len(nums) and nums[i] == num:
                if subsequences[end][-1] == num-1:
                    subsequences[end].append(num)
                    i += 1
                end -= 1
            
            while i < len(nums) and nums[i] == num:
                subsequences.append([num])
                i += 1

        for subsequence in subsequences:
            if len(subsequence) < consecutiveLength:
                return False

        return True
"""
