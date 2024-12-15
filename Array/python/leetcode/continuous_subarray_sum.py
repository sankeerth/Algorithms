"""
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose 
elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""
from typing import List
from collections import defaultdict


class Solution:
    """
    Running sum from first element to index i : sum_i. If we mod k, it will be some format like : sum_i = k * x + modk_1
    Running sum from first element to index j : sum_j. If we mod k, it will be some format like : sum_j = k * y + modk_2
    If they have the same mod, which is modk_1 == modk_2, subtracting these two running sum we get the difference sum_i - sum_j = (x - y) * k = constant * k, 
    and the difference is the sum of elements between index i and j, and the value is a multiple of k.
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runningSumMap = {0: -1} # test case: [23,2,4,6,6] and k=7
        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            if k != 0:
                runningSum = runningSum % k
            
            if runningSum in runningSumMap:
                if i - 1 > runningSumMap[runningSum]: # make sure at least 2 elements in subarray
                    return True
            else:
                runningSumMap[runningSum] = i
        
        return False


sol = Solution()
print(sol.checkSubarraySum([23,2,4,6,7], 6))
print(sol.checkSubarraySum([23,2,6,4,7], 6))
print(sol.checkSubarraySum([23,2,6,4,7], 13))
# failed testcases
print(sol.checkSubarraySum([5,0,0,0], 3))
print(sol.checkSubarraySum([1,2,12], 6))
print(sol.checkSubarraySum([23,2,4,6,6], 7))
print(sol.checkSubarraySum([1,3,0,6], 6))


"""
My solution (TLE):

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSumMap = defaultdict(int)
        prefixSumMap[nums[0]] = 0
        prefixSum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prefixSum += num
            if num == 0:
                if nums[i-1] == 0:
                    return True
                continue
            if prefixSum % k == 0:
                return True
            else:
                tempSum = prefixSum
                while tempSum > k:
                    if tempSum-k in prefixSumMap and i-1 > prefixSumMap[tempSum-k]:
                        return True
                    tempSum -= k
            
            prefixSumMap[prefixSum] = i
        
        return False
"""
