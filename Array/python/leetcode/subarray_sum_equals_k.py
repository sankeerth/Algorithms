"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number 
of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefix = 0, 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        for i in range(len(nums)):
            prefix += nums[i]
            if (prefix-k) in prefixSum:
                res += prefixSum[prefix-k]
            # this has to be after the above check else, it fails for [1], k=0
            # because we add 0:1 to the map to account for 0s in the nums
            prefixSum[prefix] += 1

        return res


sol = Solution()
print(sol.subarraySum([1], 0)) # 0
print(sol.subarraySum([1, 0], 0)) # 1
print(sol.subarraySum([1,-2,1], 0)) # 1
print(sol.subarraySum([1,1,1], 2)) # 2
print(sol.subarraySum([1,2,3], 3)) # 2
print(sol.subarraySum([1,-1,5,-2,3], 3)) # 3
print(sol.subarraySum([-3,2,1,1,2], 3)) # 3
print(sol.subarraySum([-3,2,1,1,2,1,2,-5,-4,7,3], 3)) # 9
print(sol.subarraySum([1,2,1,2,1], 3)) # 4
print(sol.subarraySum([11,1,-35,-99,75,-81,-97,16,-67,-53,429], 100)) # 1


"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
            
        counter = Counter(prefixSum)
        res = 0
        
        # ** This solution does not work for [1], 0 or [1,0], 0 **
        # since prefixSum array is generated before hand and prefix-k 
        # will be the number itself which will be present in the counter

        for prefix in counter:
            # this condition is needed when prefix count is k starting from beginning
            # since we do not have an additional 0 in the counter. However, if we add an additional
            # 0 to the counter then it will lead to incorrect result leading to additional count when
            # prefixSum == k. Ex nums: [1,-1,5,-2,3] or [0,1,-1,5,-2,3]
            if prefix == k:
                res += 1
            if (prefix - k) in counter:
                res += counter[prefix-k]

        return res

Another solution that stores prefixSum count on the fly. This is possible since subarrays 
are counted only once corresponding to the prefix sum encountered.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = defaultdict(int)
        res, prefixSum = 0, 0

        for num in nums:
            prefixSum += num
            if prefixSum == k:
                res += 1
            if (prefixSum - k) in prefixSumCount:
                res += prefixSumCount[prefixSum-k]

            prefixSumCount[prefixSum] += 1

        return res
"""
