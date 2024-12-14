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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def neighbors(i, j):
            for x, y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y
        
        def dfs(i, j, ocean):
            ocean.add((i,j))
            for x, y in neighbors(i, j):
                if (x,y) not in ocean and heights[x][y] >= heights[i][j]:
                    dfs(x, y, ocean)

        # iterate for rows
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows-1, j, atlantic)

        # iterate for columns
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)

        # list which will have both the coordinates
        return list(pacific.intersection(atlantic))          


s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
