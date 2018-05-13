"""
632. Smallest Range

You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
"""


from heapq import heappush, heappop


class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []

        heap = list()
        max_in_heap = float('-inf')

        for i in range(len(nums)):
            heappush(heap, (nums[i][0], i, 0))
            max_in_heap = max(max_in_heap, nums[i][0])

        diff = max_in_heap - heap[0][0]
        result = [heap[0][0], max_in_heap]

        while True:
            heap_min = heappop(heap)
            list_num = heap_min[1]
            index = heap_min[2]
            index += 1
            if index >= len(nums[list_num]):
                break

            heappush(heap, (nums[list_num][index], list_num, index))
            max_in_heap = max(max_in_heap, nums[list_num][index])

            if max_in_heap - heap[0][0] < diff:
                result[0] = heap[0][0]
                result[1] = max_in_heap
                diff = max_in_heap - heap[0][0]

        return result


sol = Solution()
print(sol.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
