"""
853. Car Fleet

N cars are going to the same destination along a one lane road.  The destination is target miles away.
Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.
A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.
The distance between these two cars is ignored - they are assumed to have the same position.
A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
How many car fleets will arrive at the destination?

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:
0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
"""
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev, res = 0, 0
        posAndSpeed, timeToReach = [], []

        for pos, spd in zip(position, speed):
            posAndSpeed.append((pos, spd))

        posAndSpeed.sort(reverse=True, key=lambda x: (x[0], x[1]))
        
        for pos, spd in posAndSpeed:
            timeToReach.append((target - pos) / spd)

        for time in timeToReach:
            if time > prev:
                res += 1
                prev = time

        return res


sol = Solution()
print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(sol.carFleet(10, [0,4,2], [2,1,3]))


"""
Good explanation:
https://leetcode.com/problems/car-fleet/discuss/255589/Python-Code-with-Explanations-and-Visualization-Beats-95
"""

"""
class Solution:
    def carFleet(self, target, pos, speed):
        time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res
"""

"""
Heap solution:

from heapq import heappush, heappop

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        heap = []

        for i in range(len(position)):
            heappush(heap, (-1 * position[i], speed[i]))
        
        time = 0
        while heap:
            pos, sp = heappop(heap)

            t = (target+pos) / sp
            if t > time:
                fleet += 1
                time = t

        return fleet
"""
