"""
435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need 
to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

Constraints:
1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-2 * 104 <= starti < endi <= 2 * 104
"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res

        intervals.sort(key=lambda x: (x[0], x[1]))
        prev_e = intervals[0][1]
        for cur_s, cur_e in intervals[1:]:
            if cur_s < prev_e:
                if cur_e < prev_e:
                    prev_e = cur_e
                res += 1
            else:
                prev_e  = cur_e

        return res


s = Solution()
print(s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))
print(s.eraseOverlapIntervals([[0,4],[1,2],[2,3],[3,5]])) # imp test case


"""
My other solution: Sort by end interval

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res

        intervals.sort(key=lambda x: (x[1], x[0]))
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
            else:
                prevEnd = end

        return res
"""
