"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
"""
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        heap = []
        intervals.sort()
        heapq.heappush(heap, intervals[0][1])
        res = 1

        for start, end in intervals[1:]:
            while heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            res = max(res, len(heap))

        return res


s = Solution()
print(s.minMeetingRooms([[0,5],[4,10]]))
print(s.minMeetingRooms([[0,5],[5,10]]))
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(s.minMeetingRooms([[7,10],[2,4]]))
print(s.minMeetingRooms([[6,17],[8,9],[11,12],[6,9]]))
print(s.minMeetingRooms([[26,29],[19,26],[19,28],[4,19],[4,25]]))
print(s.minMeetingRooms([[9,10],[4,9],[4,17]]))
print(s.minMeetingRooms([[13,15],[1,13]]))
print(s.minMeetingRooms([[11,20],[4,19],[13,17],[6,13]]))
print(s.minMeetingRooms([[13,15],[1,13],[6,9]]))


"""
Approach 2: Chronological Ordering
Intuition

The meeting timings given to us define a chronological order of events throughout the day. 
We are given the start and end timings for the meetings which can help us define this ordering.
Arranging the meetings according to their start times helps us know the natural order of meetings 
throughout the day. However, simply knowing when a meeting starts doesn't tell us much about its duration.

We also need the meetings sorted by their ending times because an ending event essentially tells us that 
there must have been a corresponding starting event and more importantly, an ending event tell us that 
a previously occupied room has now become free.

A meeting is defined by its start and end times. However, for this specific algorithm, we need to treat 
the start and end times individually. This might not make sense right away because a meeting is defined 
by its start and end times. If we separate the two and treat them individually, then the identity of 
a meeting goes away. This is fine because:

When we encounter an ending event, that means that some meeting that started earlier has ended now. We are not 
really concerned with which meeting has ended. All we need is that some meeting ended thus making a room available.

Let us consider the same example as we did in the last approach. 
We have the following meetings to be scheduled: (1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30). 
As before, the first diagram show us that the first three meetings are colliding with each other and they 
have to be allocated separate rooms.

Algorithm

Separate out the start times and the end times in their separate arrays.
Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. 
They will be treated individually now. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. 
The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. 
If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. 
Otherwise, we have to allocate a new room.
If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
Repeat this process until s_ptr processes all of the meetings.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms


My version of the same one using max and diff b/w start and end pointers:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start_intervals = sorted([start for start, _ in intervals])
        end_intervals = sorted([end for _, end in intervals])

        s_ptr, e_ptr, res = 0, 0, 0
        while s_ptr < len(start_intervals):
            start = start_intervals[s_ptr]
            while start >= end_intervals[e_ptr]:
                e_ptr += 1

            s_ptr += 1
            res = max(res, s_ptr - e_ptr)

        return res
"""
