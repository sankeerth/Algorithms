"""
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# See figure in leetcode
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# See figure in leetcode
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        length = len(heights)
        less_to_left, less_to_right = [0] * length, [0] * length
        less_to_right[length-1] = length
        less_to_left[0] = -1

        for i in range(1, length):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_to_left[p]
            less_to_left[i] = p

        for i in range(length-2, -1, -1):
            p = i+1
            while p < length and heights[p] >= heights[i]:
                p = less_to_right[p]
            less_to_right[i] = p

        result = 0

        for i in range(length):
            result = max(result, heights[i] * (less_to_right[i] - less_to_left[i] - 1))

        return result


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))

'''
def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
'''

'''
My solution which is O(n^2) or precisely (n*(n+1))/2 steps in for loop

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        max_height = float('-inf')
        
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(heights[j], min_height)
                max_height = max(heights[j], min_height * ((j-i)+1), max_height)
        
        return max_height
'''
