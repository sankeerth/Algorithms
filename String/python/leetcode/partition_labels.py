"""
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""


class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = list()
        char_dict = dict()
        for i, c in enumerate(S):
            if c in char_dict:
                char_dict[c][1] = i
            else:
                char_dict[c] = [i, i]

        def merge(intervals):
            intervals = sorted(intervals, key=lambda x: x[0])
            result = list()
            result.append(intervals[0])

            for interval in intervals:
                if interval[0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1], interval[1])
                else:
                    result.append(interval)

            return result

        merged = merge(char_dict.values())
        for m in merged:
            result.append(m[1]-m[0]+1)

        return result


sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("abcadefdzy"))
print(sol.partitionLabels("abcdefzy"))
print(sol.partitionLabels("abcdefazya"))


'''
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
'''