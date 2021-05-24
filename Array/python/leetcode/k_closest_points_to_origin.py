"""
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique 
(except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
from typing import List
from heapq import heappush, heappop


# Divide and conquer approach
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []

        def kClosestRecursive(points):
            res = []
            N = len(points)
            if N == 1:
                x, y = points[0][0], points[0][1]
                res.append((x ** 2 + y ** 2, points[0]))
                return res

            mid = N // 2
            left = kClosestRecursive(points[:mid])
            right = kClosestRecursive(points[mid:])

            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            while l < len(left):
                res.append(left[l])
                l += 1

            while r < len(right):
                res.append(right[r])
                r += 1

            return res

        count = 0
        res = kClosestRecursive(points)
        while count < K:
            result.append(res[count][1])
            count += 1

        return result


s = Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
print(s.kClosest([[1,3],[-2,2]], 1))


"""
O(n + k logn) solution using heap

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result, heap = [], []
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            dist = x ** 2 + y ** 2
            heappush(heap, (dist, i))

        while K > 0:
            top = heappop(heap)
            index = top[1]
            result.append(points[index])
            K -= 1

        return result
"""

"""
O(n logk) solution using heap

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res, heap = [], []
        for i, x, y in enumerate(points):
            dist = x * x + y * y
            heappush(heap, (-dist, i))
            if len(heap) > k:
                heappop(heap)
        
        for _, i in heap:
            res.append(points[i])

        return res
"""
