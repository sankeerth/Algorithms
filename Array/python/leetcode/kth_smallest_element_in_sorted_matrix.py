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

"""
Leetcode solution (similar to the solution above expect that heap is constructed with elements from some/all rows):

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # The size of the matrix
        N = len(matrix)
        
        # Preparing our min-heap
        minHeap = []
        for r in range(min(k, N)):
            
            # We add triplets of information for each cell
            minHeap.append((matrix[r][0], r, 0))
        
        # Heapify our list
        heapq.heapify(minHeap)    
        
        # Until we find k elements
        while k:
            
            # Extract-Min
            element, r, c = heapq.heappop(minHeap)
            
            # If we have any new elements in the current row, add them
            if c < N - 1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            
            # Decrement k
            k -= 1
        
        return element

Complexity Analysis

Time Complexity: let X=min(K,N); X + K log(X)

Well the heap construction takes O(X) time.

After that, we perform K iterations and each iteration has two operations. 
We extract the minimum element from a heap containing X elements. 
Then we add a new element to this heap. Both the operations will take O(log(X)) time.

Thus, the total time complexity for this algorithm comes down to be O(X + Klog(X)) where X is min(K,N).

Space Complexity: O(X) which is occupied by the heap.
"""

"""
Check Binary Search solution in:

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C++):-Easy-to-understand-solutions-using-Heap-and-Binary-Search
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/

class Solution:
    def countLessEqual(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
               
                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
                
            else:
                
                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid
                
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start

Complexity Analysis

Time Complexity: O(N×log(Max−Min))

Let's think about the time complexity in terms of the normal binary search algorithm. 
For a one-dimensional binary search over an array with NN elements, the complexity comes out to be O(log(N)).

For our scenario, we are kind of defining our binary search space in terms of the minimum and the maximum numbers in the array. 
Going by this idea, the complexity for our binary search should be O(log(Max−Min)) 
where Max is the maximum element in the array and likewise, Min is the minimum element.

However, we update our search space after each iteration. So, even if the maximum element is super large as compared to the remaining 
elements in the matrix, we will bring down the search space considerably in the next iterations. But, going purely by the extremes 
for our search space, the complexity of our binary search in search of Kth smallest element will be O(log(Max−Min)).

In each iteration of our binary search approach, we iterate over the matrix trying to determine the size of the left-half 
as explained before. That takes O(N).

Thus, the overall time complexity is O(N×log(Max−Min))

Space Complexity: O(1)O(1) since we don't use any additional space for performing our binary search.
"""
