"""
378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5 

Constraints:
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
"""
from typing import List
import heapq


# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/986296/CPP-solution-O(klogn)-simple-to-understand-based-on-%40StefanPochmann's-idea.
class Solution:
    """
    Complexity: O(k logn) where n is the number of rows
    If the first (~n) smallest elements are the first element of each row, then
    number of elements in the heap will be equal to n since one element from each row is present
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        N, count = len(matrix), 1

        while heap:
            num, i, j = heapq.heappop(heap)
            if count == k:
                return num

            if j+1 < N:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
            if j == 0 and i+1 < N:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
            
            count += 1
        

s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 9))
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 4))
print(s.kthSmallest([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 8))
print(s.kthSmallest([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 14))
print(s.kthSmallest([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 19))


"""
Check O(k) 'complicated solution and proof' when you have time:
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/O(n)-from-paper.-Yes-O(rows).
"""
