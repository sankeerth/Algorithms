"""
974. Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) 
subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""
from typing import List


"""
Very good white-board explanation of the solution with the need to store and add frequencies of reminders.
https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/413234/DETAILED-WHITEBOARD!-BEATS-100-(Do-you-really-want-to-understand-It)
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res, prefix = 0, 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k
            if prefix in prefixSum:
                res += prefixSum[prefix]
            # this has to be after the above check
            prefixSum[prefix] += 1

        return res


sol = Solution()
print(sol.subarraysDivByK([4,5,0], 5))
print(sol.subarraysDivByK([-2,-3,0], 5))
print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))


"""
O(n^2) solution:

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        for i in range(len(A)):
            total = A[i]
            if total % K == 0:
                res += 1
            for j in range(i+1, len(A)):
                total += A[j]
                if total % K == 0:
                    res += 1

        return res
"""
