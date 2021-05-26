"""
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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


"""
Similar to leetcode solution that counts up for the least number in consecutive sequence:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
"""

"""
O(n) solution recursive:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        countIntegersBelowItself = {}
        for num in nums:
            if num not in countIntegersBelowItself:
                countIntegersBelowItself[num] = 0

        def longestConsecutiveRecursive(num):
            if countIntegersBelowItself[num] != 0:
                return countIntegersBelowItself[num]

            count = 1
            if num-1 in countIntegersBelowItself:
                count = longestConsecutiveRecursive(num-1) + 1

            countIntegersBelowItself[num] = count
            return count

        res = 0
        for num in nums:
            count = longestConsecutiveRecursive(num)
            res = max(res, count)

        return res
"""
