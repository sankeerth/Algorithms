"""
444. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. 
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. 
Reconstruction means building a shortest common supersequence of the sequences in seqs 
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it). 
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

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
1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.
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
