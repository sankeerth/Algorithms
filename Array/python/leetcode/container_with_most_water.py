"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, i, j = 0, 0, len(height)-1

        while i < j:
            left, right = height[i], height[j]
            h, w = min(left, right), j-i
            res = max(res, h * w)
            
            if left < right:
                i += 1
            else:
                j -= 1

        return res


sol = Solution()
print(sol.maxArea([2,4,3,6,9,5]))
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
print(sol.maxArea([4,3,2,1,4]))
print(sol.maxArea([1,2,1]))


"""
My O(N) solution with O(N) space:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        maxFromLeft, maxFromRight = [0] * len(height), [0] * len(height)
        maxFromLeft[0], maxFromRight[-1] = height[0], height[-1]
        
        for i in range(1, len(height)):
            maxFromLeft[i] = max(maxFromLeft[i-1], height[i])
            maxFromRight[len(height)-i-1] = max(maxFromRight[len(height)-i], height[len(height)-i-1])

        left, right = 0, len(height)-1
        while left < right:
            h, w = min(maxFromLeft[left], maxFromRight[right]), right - left
            res = max(res, h * w)
            if maxFromLeft[left] < maxFromRight[right]:
                left += 1
            else:
                right -= 1

        return res
"""
