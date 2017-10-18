"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        j = len(height) - 1
        i = 0

        max_val = 0
        while i < j:
            val_i = height[i]
            val_j = height[j]
            max_val = max(max_val, min(val_i, val_j) * (j - i))
            if val_i < val_j:
                i += 1
            else:
                j -= 1

        return max_val

sol = Solution()
print(sol.maxArea([2,4,3,6,9,5]))
