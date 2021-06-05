"""
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# See figure in leetcode
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# See figure in leetcode
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
from typing import List


class Solution(object):
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        res, length = 0, len(heights)
        lessToLeft, lessToRight = [0] * length, [0] * length
        lessToRight[length-1] = length
        lessToLeft[0] = -1

        for i in range(1, length):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessToLeft[p]
            lessToLeft[i] = p

        for i in range(length-2, -1, -1):
            p = i+1
            while p < length and heights[p] >= heights[i]:
                p = lessToRight[p]
            lessToRight[i] = p

        for i in range(length):
            h = heights[i]
            w = lessToRight[i] - lessToLeft[i] - 1
            res = max(res, h * w)

        return res


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(sol.largestRectangleArea([2, 1, 5, 6, 3, 3]))
print(sol.largestRectangleArea([1, 2, 3, 4, 5]))
print(sol.largestRectangleArea([2, 4]))


"""
Leetcode solution using stack: O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i, res = 0, 0
        stack = [-1]
        heights.append(0) # to ensure that the remaining elements are popped at the end

        while i < len(heights):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                w = i - stack[-1] - 1
                h = heights[top]
                res = max(res, h * w)
            stack.append(i)
            i += 1

        return res
"""

"""
My solution which is O(n^2) or precisely (n*(n+1))/2 steps in for loop

class Solution(object):
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        max_height = float('-inf')
        
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(heights[j], min_height)
                max_height = max(heights[j], min_height * ((j-i)+1), max_height)
        
        return max_height
"""
