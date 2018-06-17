"""
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        visited = {num: False for num in nums}
        result = 0

        for num in nums:
            if num in num_set and not visited[num]:
                count = 1
                visited[num] = True
                prev = num-1
                next = num+1

                while prev in num_set:
                    prev -= 1
                    count += 1
                    visited[prev] = True

                while next in num_set:
                    next += 1
                    count += 1
                    visited[next] = True

                result = max(result, count)

        return result


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([100, 200, 1, 5, 3]))
print(sol.longestConsecutive([100, 200, 1, 5, 2]))
print(sol.longestConsecutive([]))

'''
My other solution:

class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
'''
