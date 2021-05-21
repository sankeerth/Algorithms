"""
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:
1 <= nums1.length, nums2.length <= 104
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue, res, seen = [], [], set()
        heappush(queue, (nums1[0] + nums2[0], 0, 0))
        seen.add((0, 0))

        while queue and len(res) < k:
            _, i, j = heappop(queue)
            res.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in seen:
                heappush(queue, (nums1[i+1] + nums2[j], i+1, j))
                seen.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in seen:
                seen.add((i, j+1))
                heappush(queue, (nums1[i] + nums2[j+1], i, j+1))

        return res


sol = Solution()
print(sol.kSmallestPairs([1,7,11], [2,4,6], 3))
print(sol.kSmallestPairs([1,1,2], [1,2,3], 2))
print(sol.kSmallestPairs([1,2], [3], 3))
print(sol.kSmallestPairs([1,1,2], [1,2,3], 10))


"""
Leetcode discuss solution:

The previous solution right away considered (the first pair of) all matrix rows 
(see visualization above). This one doesn't. It starts off only with the very first pair 
at the top-left corner of the matrix, and expands from there as needed. Whenever a pair 
is chosen into the output result, the next pair in the row gets added to the priority 
queue of current options. Also, if the chosen pair is the first one in its row, 
then the first pair in the next row is added to the queue.

Here's a visualization of a possible state:

# # # # # ? . .
# # # ? . . . .
# ? . . . . . .   "#" means pair already in the output
# ? . . . . . .   "?" means pair currently in the queue
# ? . . . . . .
? . . . . . . .
. . . . . . . .
As I mentioned in the comments, that could be further improved. Two of those ? don't actually need to be in the queue yet. I'll leave that as an exercise for the reader :-)

    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
"""
