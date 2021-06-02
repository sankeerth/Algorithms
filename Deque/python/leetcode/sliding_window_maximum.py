"""
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:
Input: nums = [9,11], k = 2
Output: [11]

Example 5:
Input: nums = [4,-2], k = 2
Output: [4]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from typing import List


class Solution(object):
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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        res, maxFromLeft, maxFromRight = [0] * (len(nums)-k+1), [0] * len(nums), [0] * len(nums)
        curMax = nums[0]

        for i in range(len(nums)):
            if i % k == 0:
                curMax = nums[i]
            
            curMax = max(curMax, nums[i])
            maxFromLeft[i] = curMax

        curMax = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if (i+1) % k == 0:
                curMax = nums[i]
            
            curMax = max(curMax, nums[i])
            maxFromRight[i] = curMax
        
        for i in range(len(nums)-k+1):
            res[i] = max(maxFromLeft[i+k-1], maxFromRight[i])

        return res


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(sol.maxSlidingWindow([3,3,5,5,6,7], 3))
print(sol.maxSlidingWindow([9,6,11,8,10,5,4,13,93,14], 4))


"""
Using Deque:

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, dq = [], deque()
        if not nums:
            return res

        dq.append(0)        
        for i in range(1, k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq[0] <= i - k:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])

        return res
"""
