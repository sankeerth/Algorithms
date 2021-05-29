"""
452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons spread in two-dimensional space. For each balloon, 
provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, 
y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. 
The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. 
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows 
that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2

Constraints:
1 <= points.length <= 104
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res, heap = 0, []
        for point in points:
            heappush(heap, point)

        while heap:
            start, end = heappop(heap)
            while heap and start <= heap[0][0] <= end:
                nextStart, nextEnd = heappop(heap)
                start = max(start, nextStart)
                end = min(end, nextEnd)
            res += 1

        return res


sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(sol.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])) # failed testcase


"""
Leetcode solution using sort, which is simpler and memory efficient:

Greedy problems usually look like "Find minimum number of something to do something" or 
"Find maximum number of something to fit in some conditions", and typically propose an unsorted input.

The standard solution has \mathcal{O}(N \log N)O(NlogN) time complexity and consists of two parts:
Figure out how to sort the input data O(NlogN) time). That could be done directly by a sorting or indirectly by a heap usage. 
Typically sort is better than the heap usage because of gain in space.
Parse the sorted input to have a solution (\mathcal{O}(N)O(N) time).

Intuition

Let's sort the balloons by the end coordinate, and then check them one by one. The first balloon is a green one number 0, it ends at coordinate 6, and there is no balloons ending before it because of sorting.

The other balloons have two possibilities :
To have a start coordinate smaller than 6, like a red balloon. These ones could be burst together with the balloon 0 by one arrow.
To have a start coordinate larger than 6, like a yellow balloon. These ones couldn't be burst together with the balloon 
0 by one arrow, and hence one needs to increase the number of arrows here.

That means that one could always track the end of the current balloon, and ignore all the balloons which 
end before it. Once the current balloon is ended (= the next balloon starts after the current balloon), 
one has to increase the number of arrows by one and start to track the end of the next balloon.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        end = points[0][1]
        arrows = 1

        for s, e in points:
            if end < s:
                arrows += 1
                end = e

        return arrows
"""
