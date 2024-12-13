"""
444. Sequence Reconstruction

You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n]. You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.

Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences for the given array sequences.

For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences, [1,2,3] and [1,3,2].
While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
Return true if nums is the only shortest supersequence for sequences, or false otherwise.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, 
because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].

Example 3:
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true

Constraints:
n == nums.length
1 <= n <= 104
nums is a permutation of all the integers in the range [1, n].
1 <= sequences.length <= 104
1 <= sequences[i].length <= 104
1 <= sum(sequences[i].length) <= 105
1 <= sequences[i][j] <= n
All the arrays of sequences are unique.
sequences[i] is a subsequence of nums.
"""
from typing import List


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not seqs:
            return False

        if len(org) <= 1:
            for seq in seqs:
                if seq != org:
                    return False
            return True

        sequencesToBeMaintained = set()
        positions= {}
        for i in range(len(org)-1):
            positions[org[i]] = i
            sequencesToBeMaintained.add((org[i], org[i+1]))
        positions[org[-1]] = len(org)-1

        for seq in seqs:
            if len(seq) == 1:
                if seq[0] not in positions:
                    return False
            else:
                for i in range(len(seq)-1):
                    if seq[i] not in positions or seq[i+1] not in positions or positions[seq[i]] > positions[seq[i+1]]:
                        return False
                    sequence = (seq[i], seq[i+1])
                    if sequence in sequencesToBeMaintained:
                        sequencesToBeMaintained.remove((sequence))

        return True if not sequencesToBeMaintained else False


sol = Solution()
print(sol.sequenceReconstruction([1,2,3], [[1,2],[1,3]]))
print(sol.sequenceReconstruction([1,2,3], [[1,2]]))
print(sol.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]]))
print(sol.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,5,2],[1,5],[4]]))
print(sol.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,5,2],[1,5],[4,1]]))
print(sol.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]))
print(sol.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2],[2,5]]))
print(sol.sequenceReconstruction([1], [[0]]))
print(sol.sequenceReconstruction([1], [[1]]))
print(sol.sequenceReconstruction([1], [[2]]))
print(sol.sequenceReconstruction([1,2], [[1,2],[2,1]]))
print(sol.sequenceReconstruction([1], [[1],[1],[1]]))


"""
Leetcode discuss solution using Topological sort:

Thought process:

Construct the dependency graph using seqs
Try topological sorting on the dependency graph
    During each step, check whether there is only one option to select the node
    If there is more than one options, return False directly
After getting the topological sorted node list, check whether its length is the same with number 
of distinct values and whether it's the same with org

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        values = {val for seq in seqs for val in seq}
        graphs = {val:[] for val in values}
        indegrees = {val:0 for val in values}
        for seq in seqs:
            for i in range(len(seq)-1):
                s, t = seq[i], seq[i+1] # source, target
                graphs[s].append(t)
                indegrees[t] += 1
        stack = []
        for val, degree in indegrees.items():
            if degree == 0:
                stack.append(val)
        res = []
        while stack:
            # there can only be one result of topological sort
            if len(stack) > 1:
                return False
            s = stack.pop() # source
            res.append(s)
            for t in graphs[s]: # target
                indegrees[t] -= 1
                if indegrees[t] == 0:
                    stack.append(t)
        return len(res) == len(values) and res == org
"""
