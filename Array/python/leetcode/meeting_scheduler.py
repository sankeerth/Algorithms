"""
1229. Meeting Scheduler

Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, 
return the earliest time slot that works for both of them and is of duration duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
It is guaranteed that no two availability slots of the same person intersect with each other. 
That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

Constraints:
1 <= slots1.length, slots2.length <= 104
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 109
1 <= duration <= 106
"""
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        res = []
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        first, second = 0, 0
        while first < len(slots1) and second < len(slots2):
            firstStart, firstEnd = slots1[first][0], slots1[first][1]
            secondStart, secondEnd = slots2[second][0], slots2[second][1]

            if firstEnd < secondStart:
                first += 1
            elif secondEnd < firstStart:
                second += 1
            else:
                maxStart = max(firstStart, secondStart)
                minEnd = min(firstEnd, secondEnd)
                maxOverlapDuration = minEnd - maxStart

                if maxOverlapDuration >= duration:
                    res = [maxStart, maxStart + duration]
                    break

                if firstEnd < secondEnd:
                    first += 1
                else:
                    second += 1
        
        return res


sol = Solution()
print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))
print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 6))
print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12))
print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 11))


"""
Leetcode solution using Heap:

The key idea here is that we only need one heap. That is, we can put the time slots for both people into the same heap, 
and then if we find a common time slot, we know that the two-time slots couldn't possibly be for the same person. 
Before reading the justification for this, have a think for yourself about why we can draw such a bold conclusion.

The problem description states that the time slots for a single person do not overlap. This means that if, for example, 
we have the time slots [10, 15] and [14, 20], then we know that these time slots cannot be for the same person. 
Otherwise, we would have a contradiction. So, given that a common time slot has to overlap, the two slots have to be from different people.

Algorithm
Initialize a heap timeslots and push time slots that last longer than duration into it.
Iterate until there's only one time slot remaining in timeslots:
Pop the first time slot [start1, end1] from timeslots.
Retrieve the next time slot [start2, end2], which is the current top element in timeslots.
If we find end1 >= start2 + duration, because start1 <= start2, the common slot is longer than duration and we can return it.
If we don't find the common slot that is longer than duration, return an empty array.


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # build up a heap containing time slots last longer than duration
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []
"""
