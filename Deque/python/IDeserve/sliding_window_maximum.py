"""
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
"""

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        max_values = list()
        dq = deque()
        dq.append(0)

        for i in range(1, k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        max_values.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq[0] <= i - k:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            max_values.append(nums[dq[0]])

        return max_values

sol = Solution()
print(sol.maxSlidingWindow([3,3,5,5,6,7], 3))
print(sol.maxSlidingWindow([9,6,11,8,10,5,4,13,93,14], 4))
