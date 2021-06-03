"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        maxFromLeft, maxFromRight = [0] * len(height), [0] * len(height)
        maxFromLeft[0], maxFromRight[-1] = height[0], height[-1]

        for i in range(1, len(height)):
            maxFromLeft[i] = max(maxFromLeft[i-1], height[i])
        
        for i in range(len(height)-2, -1, -1):
            maxFromRight[i] = max(maxFromRight[i+1], height[i])

        for i in range(len(height)):
            res += min(maxFromLeft[i], maxFromRight[i]) - height[i]

        return res

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([2,4,3,6,9,5]))


"""
Leetcode solution using Stack:

We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, 
which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, 
we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and 
add resulting trapped water to ans.

Algorithm:
Use stack to store the indices of the bars.

Iterate the array:
While stack is not empty and height[current]>height[st.top()]
It means that the stack element can be popped. Pop the top element as top.
Find the distance between the current element and the element at top of stack, which is to be filled. distance=current−st.top()−1
Find the bounded height bounded_height=min(height[current],height[st.top()])−height[top]
Add resulting trapped water to answer ans+=distance×bounded_height
Push current index to top of the stack
Move current to the next position

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                    h = min(height[i], height[stack[-1]]) - height[top]
                    res += w * h

            stack.append(i)

        return res
"""

"""
Leetcode solution: O(n) time, O(1) space
Similar to the solution on top with maxFromLeft and maxFromRight using one variable instead of an array

instead of calculating area by height*width, we can think it in a cumulative way.
In other words, sum water amount of each bin(width=1).
Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container.
Fix the higher one and flow water from the lower part.
For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.

class Solution:
    def trap(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height)-1
        leftMax, rightMax = 0, 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                right -= 1

        return res
"""
