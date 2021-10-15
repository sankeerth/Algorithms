"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" 
touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) 
from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:
Given the following 5x5 matrix:
  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from typing import List


'''
Instead of figuring out which cells can flow water to ocean, let's look at the problem as 
figuring out cells where water may reach from both oceans. Of course, we need to reverse the 
height check i.e. water can flow from a cell with height h to another neighbor cell with height >= h.

Cells directly connected to Pacific ocean are first row and first column so they become our start cells. 
We can do a DFS/BFS from these start cells to figure out all the reachable cells. 
Atlantic ocean is similar - we just need to treat last row and last column as start cells.
Finally, we iterate over all the cells and add the ones that were visited by both traversals to the result.
'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        if not matrix or not matrix[0]:
            return result

        m, n = len(matrix), len(matrix[0])
        pacific, atlantic = set(), set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # define left, right, up, down

        def dfs(x, y, ocean):
            ocean.add((x, y))
            for dx, dy in directions:
                i, j = x + dx, y + dy
                # if the coordinates are valid and if c(i) > c (i-1)
                if 0 <= i < m and 0 <= j < n and (i, j) not in ocean and matrix[i][j] >= matrix[x][y]:
                    dfs(i, j, ocean)

        # iterate for rows
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)

        # iterate for columns
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m-1, i, atlantic)

        # list which will have both the coordinates
        return list(pacific.intersection(atlantic))


s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
