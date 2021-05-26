"""
632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Example 3:
Input: nums = [[10,10],[11,11]]
Output: [10,11]

Example 4:
Input: nums = [[10],[11]]
Output: [10,11]

Example 5:
Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]

Constraints:
    nums.length == k
    1 <= k <= 3500
    1 <= nums[i].length <= 50
    -105 <= nums[i][j] <= 105
    nums[i] is sorted in non-decreasing order.
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for i, item in enumerate(nums):
            num = item[0]
            heappush(heap, (num, i, 0))

        minRange, maxRange = heap[0][0], max(heap, key=lambda x: x[0])[0]
        low, high = minRange, maxRange

        while heap:
            _, row, index = heappop(heap)
            if index+1 < len(nums[row]):
                num = nums[row][index+1]
                heappush(heap, (num, row, index+1))
                
                high = max(high, num)
            # can be used to break out of loop sooner since num in other lists are in sorted order and only going to be greater
            # Hence, it is not possible to find a smaller range than the one already found
            #     low = heap[0][0] 
            # else:
            #     break

            # to update the low only when there are nums from all k lists in heap.
            # once one of the list is out of bounds, previously calculate low will stay for the remaining duration
            if len(heap) == len(nums):
                low = heap[0][0]

            if high - low < maxRange - minRange:
                minRange, maxRange = low, high

        return [minRange, maxRange]


sol = Solution()
print(sol.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))
print(sol.smallestRange([[10,10],[11,11]]))
print(sol.smallestRange([[10],[11]]))
print(sol.smallestRange([[1],[2],[3],[4],[5],[6],[7]]))
print(sol.smallestRange([[4]]))
