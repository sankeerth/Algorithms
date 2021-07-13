"""
1610. Maximum Number of Visible Points

You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.
Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. 
Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. 
Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].
You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.
There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.
Return the maximum number of points you can see.

Example 1:
Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.

Example 2:
Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.

Example 3:
Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.

Constraints:
1 <= points.length <= 10^5
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100
"""
from typing import List
import math


class Solution:
    # Good explanation: https://leetcode.com/problems/maximum-number-of-visible-points/discuss/894732/Python-3-Simple-Steps
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        res, overlappingPoints = 0, 0
        degrees = []

        def calcAngleFromLocation(point):
            x1, y1 = location
            x2, y2 = point

            tan =  math.atan2((y2-y1), (x2-x1)) * (180 / math.pi)
            return (tan + 360) % 360

        for point in points:
            if point == location:
                overlappingPoints += 1
                continue
            tangent = calcAngleFromLocation(point)
            degrees.append(tangent)

        # 2. Calculate the angle between you and each point.
	    #    i.  Sort the angles from smallest to largest.
	    #    ii. Extend angles [0, 40, 355] -> [0, 40, 355, 360, 400, 715]
	    #        This allows us to see that 355 is close to 0.
        degrees = degrees + [degree + 360 for degree in degrees]
        degrees.sort()
        i, j = 0, 0

        while j < len(degrees):
            while i <= j and degrees[j] - degrees[i] > angle:
                i += 1
            
            res = max(res, j-i+1)
            j += 1

        return res + overlappingPoints


sol = Solution()
print(sol.visiblePoints([[2,1],[2,2],[3,3]], 90, [1,1]))
print(sol.visiblePoints([[2,1],[2,2],[3,4],[1,1]], 90, [1,1]))
print(sol.visiblePoints([[1,0],[2,1]], 13, [1,1]))
print(sol.visiblePoints([[1,1],[2,2],[3,3]], 0, [1,1]))
print(sol.visiblePoints([[1,2]], 0, [1,1]))
print(sol.visiblePoints([[2,1]], 0, [1,1]))
# failed test case
print(sol.visiblePoints([[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]], 0, [1,1]))
print(sol.visiblePoints([[60,61],[58,47],[17,26],[87,97],[63,63],[26,50],[70,21],[3,89],[51,24],[55,14],[6,51],[64,21],[66,33],[54,35],[87,38],[30,0],[37,92],[92,12],[60,73],[75,98],[1,11],[88,24],[82,92]], 44, [15,50]))


"""
Leetcode discuss solution using pure tangents and not converting to degrees

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        arr, extra = [], 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx))
        
        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180
        
        l = ans = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans + extra
"""
