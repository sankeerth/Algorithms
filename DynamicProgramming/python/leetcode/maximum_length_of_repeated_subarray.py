"""
718. Maximum Length of Repeated Subarray

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[0] * l2 for _ in range(l1)]
        res = 0

        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    if i == l1-1 or j == l2-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j+1] + 1

                    res = max(res, dp[i][j])

        return res 


sol = Solution()
print(sol.findLength([1,2,3,2,1], [3,2,1,4,7]))
print(sol.findLength([0,0,0,0,0], [0,0,0,0,0]))


"""
Leetcode O(n^3) solution:

class Solution(object):
    def findLength(self, A, B):
        ans = 0
        Bstarts = collections.defaultdict(list)
        for j, y in enumerate(B):
            Bstarts[y].append(j)

        for i, x in enumerate(A):
            for j in Bstarts[x]:
                k = 0
                while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
                    k += 1
                ans = max(ans, k)
        return ans
"""
