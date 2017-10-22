"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
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
