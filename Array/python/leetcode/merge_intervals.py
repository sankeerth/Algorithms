"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key= lambda x: x[0])

        res.append(intervals[0])
        for curStart, curEnd in intervals[1:]:
            prevStart, prevEnd = res[-1][0], res[-1][1]
            if curStart <= prevEnd:
                res[-1][1] = max(prevEnd, curEnd)
            else:
                res.append([curStart, curEnd])

        return res


sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,3],[2,6],[8,10],[15,18],[10,12]]))
print(sol.merge([[1,3],[2,6],[8,10],[15,18],[10,12],[9,13]]))
print(sol.merge([[1,3],[2,6],[8,10],[15,18],[0,9]]))


"""
Older signature using Interval class

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        '''
        :type intervals: List[Interval]
        :rtype: List[Interval]
        '''
        merged_intervals = list()
        if not intervals:
            return merged_intervals

        intervals.sort(key=lambda x: x.start)

        merged_intervals.append(intervals[0])
        for interval in intervals[1:]:
            if interval.start <= merged_intervals[-1].end:
                merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
            else:
                merged_intervals.append(interval)

        return merged_intervals


def create_intervals(list_of_intervals):
    intervals = list()
    for l in list_of_intervals:
        intervals.append(Interval(l[0], l[1]))

    return intervals

sol = Solution()
print(sol.merge(create_intervals([[1,3],[2,6],[8,10],[15,18]])))
print(sol.merge(create_intervals([[1,3],[2,6],[8,10],[15,18],[10,12]])))
print(sol.merge(create_intervals([[1,3],[2,6],[8,10],[15,18],[10,12],[9,13]])))
print(sol.merge(create_intervals([[1,3],[2,6],[8,10],[15,18],[0,9]])))
"""
