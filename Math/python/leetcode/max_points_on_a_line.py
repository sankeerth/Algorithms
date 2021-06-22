"""
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0

        def slope(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                return float('inf')
            
            return (y2-y1)/(x2-x1)

        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    s = slope(i, j)
                    slopes[s] += 1
            maxPoints = max(slopes.values()) if slopes else 0
            res = max(res, maxPoints + 1)

        return res


sol = Solution()
print(sol.maxPoints([[1,1],[2,2],[3,3]]))
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(sol.maxPoints([[0,0],[1,-1],[1,1]])) # failed testcase (return float('inf') fixed it instead of return x1)
