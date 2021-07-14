"""
1776. Car Fleet II

There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, 
where cars[i] = [positioni, speedi] represents:
positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. 
Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, 
which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. 
Answers within 10-5 of the actual answers are accepted.

Example 1:
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, 
and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.

Example 2:
Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]

Constraints:
1 <= cars.length <= 105
1 <= positioni, speedi <= 106
positioni < positioni+1
"""
from typing import List


class Solution:
    # very good explanation: https://leetcode.com/problems/car-fleet-ii/discuss/1085844/Python3.-Simple-solution-with-using-stack
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = []
        stack = []

        for dist, speed in cars[::-1]:
            time = float('inf')

            # pop if cur speed is less than speed at top of stack since it can never collide
            while stack and speed <= stack[-1][1]:
                stack.pop()

            # pop if the time to collision to top of stack more than the time the top of stack took to collide to a car in front of it
            # Imagine a,b,c on the road -> if the a catches b later than b catched c -> then a won't catch b but b+c
            while stack and (stack[-1][0] - dist) / (speed - stack[-1][1]) >= stack[-1][2]:
                stack.pop()

            if stack:
                nextDist, nextSpeed = stack[-1][0], stack[-1][1]
                time = (nextDist - dist) / (speed - nextSpeed)
                res.append(time)
            else:
                res.append(-1)

            stack.append([dist, speed, time])

        return res[::-1]


sol = Solution()
print(sol.getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))
print(sol.getCollisionTimes([[3,4],[5,4],[6,3],[9,1]]))
