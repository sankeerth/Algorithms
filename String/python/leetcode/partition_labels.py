"""
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each 
letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        intervals = {}
        for i, c in enumerate(S):
            if c not in intervals:
                intervals[c] = [i, i]
            intervals[c][1] = i

        sortedIntervals = sorted(intervals.values())
        mergedIntervals = [sortedIntervals[0]]

        for s, e in sortedIntervals[1:]:
            if s < mergedIntervals[-1][1]:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], e)
            else:
                mergedIntervals.append([s, e])

        res = []
        for s, e in mergedIntervals:
            res.append(e - s + 1)

        return res


sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("abcadefdzy"))
print(sol.partitionLabels("abcdefzy"))
print(sol.partitionLabels("abcdefazya"))


"""
leetcode solution:

class Solution:
    def partitionLabels(self, S):
        results = []
        last = {}

        for i in range(len(S) - 1, -1, -1):
            if S[i] not in last:
                last[S[i]] = i

        i = 0
        while i < len(S):
            j = last[S[i]]
            span = 1
            while i != j:
                i += 1
                span += 1
                j = max(j, last[S[i]])
            results.append(span)
            i += 1

        return results
"""

"""
Slightly simpler than leetcode solution (my version):

class Solution:
    def partitionLabels(self, S):
        result = []
        last = {}

        for i in range(len(string)-1, -1, -1):
            if not string[i] in last:
                last[string[i]] = i

        end, span = 0, 0
        for i, c in enumerate(string):
            if i <= end:
                end = max(end, last[c])
                span += 1
            else:
                result.append(span)
                end  = last[c]
                span = 1
                
        result.append(span)

        return result 
"""
