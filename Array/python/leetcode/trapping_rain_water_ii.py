"""
407. Trapping Rain Water II

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, 
return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small pounds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:
    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 104
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    # leetcode discuss solution: https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
    # visualization of the problem: https://leetcode.com/problems/trapping-rain-water-ii/discuss/89472/Visualization-No-Code
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        res, heapMax = 0, 0
        heap, visited = [], set()

        def neighbors(i, j):
            for x, y in [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]:
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                    yield x, y

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        while heap:
            h, i, j = heappop(heap)
            heapMax = max(heapMax, h)
            res += heapMax - h
            for x, y in neighbors(i, j):
                heappush(heap, (heightMap[x][y], x, y))
                visited.add((x, y))

        return res


sol = Solution()
print(sol.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(sol.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
