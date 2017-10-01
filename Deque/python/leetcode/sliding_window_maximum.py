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

"""
Leetcode discuss: O(n) solution in 2 passes
For Example: A = [2,1,3,4,6,3,8,9,10,12,56], w=4

partition the array in blocks of size w=4. The last block may have less then w.
2, 1, 3, 4 | 6, 3, 8, 9 | 10, 12, 56|

Traverse the list from start to end and calculate max_so_far. Reset max after each block boundary (of w elements).
left_max[] = 2, 2, 3, 4 | 6, 6, 8, 9 | 10, 12, 56

Similarly calculate max in future by traversing from end to start.
right_max[] = 4, 4, 4, 4 | 9, 9, 9, 9 | 56, 56, 56

now, sliding max at each position i in current window, sliding-max(i) = max{right_max(i), left_max(i+w-1)}
sliding_max = 4, 6, 6, 8, 9, 10, 12, 56
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        length = len(nums)
        left_max = [0] * length
        right_max = [0] * length
        max_values = list()

        curr_max = nums[0]
        for i in range(length):
            if i % k == 0:
                curr_max = nums[i]

            if curr_max >= nums[i]:
                left_max[i] = curr_max
            else:
                left_max[i] = nums[i]
                curr_max = nums[i]

        curr_max = nums[-1]
        for i in range(length - 1, -1, -1):
            if (i + 1) % k == 0:
                curr_max = nums[i]

            if curr_max >= nums[i]:
                right_max[i] = curr_max
            else:
                right_max[i] = nums[i]
                curr_max = nums[i]

        for i in range(length - k + 1):
            max_values.append(max(left_max[i + k - 1], right_max[i]))

        return max_values

sol = Solution()
print(sol.maxSlidingWindow([3,3,5,5,6,7], 3))
print(sol.maxSlidingWindow([9,6,11,8,10,5,4,13,93,14], 4))
