"""
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = []
Output: 0

Example 3:
Input: matrix = [["0"]]
Output: 0

Example 4:
Input: matrix = [["1"]]
Output: 1

Example 5:
Input: matrix = [["0","0"]]
Output: 0

Constraints:
    rows == matrix.length
    cols == matrix[i].length
    0 <= row, cols <= 200
    matrix[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    # Building on largest rectangle in histogram problem
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        heights = [0] * (cols+1)
        heights[-1] = -1

        def maxAreaOfHistogram(heights):
            maxArea, stack = 0, [-1]
            for i in range(cols+1):
                while heights[i] < heights[stack[-1]]:
                    top = stack.pop()
                    h = heights[top]
                    w = i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(i)

            return maxArea

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            maxArea = maxAreaOfHistogram(heights)
            res = max(res, maxArea)

        return res


sol = Solution()
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(sol.maximalRectangle([["0","0"]]))
print(sol.maximalRectangle([["1"]]))

"""
Leetcode solution:

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        left, right, height = [0] * cols, [cols] * cols, [0] * cols

        for i in range(rows):
            zeroFromLeft, zeroFromRight = 0, cols

            for j in range(cols):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(cols):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], zeroFromLeft)
                else:
                    left[j] = 0
                    zeroFromLeft = j + 1

            for j in range(cols-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], zeroFromRight)
                else:
                    right[j] = cols
                    zeroFromRight = j
            
            for j in range(cols):
                res = max(res, height[j] * (right[j] - left[j]))

        return res
"""
