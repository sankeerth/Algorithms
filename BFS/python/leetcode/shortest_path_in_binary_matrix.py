"""
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
"""
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: # if first or last element of grid is 1
            return -1

        rows, cols = len(grid), len(grid[0])
        xCoords = [-1, -1, 0, 1, 1, 1, 0, -1]
        yCoords = [0, 1, 1, 1, 0, -1, -1, -1]
        queue = [(0, 0, 1)]
        grid[0][0] = -1 # Visited as -1 (all zeros)

        while queue:
            top = queue.pop(0)
            count = top[2]
            if top[0] == rows-1 and top[1] == cols -1:
                return count

            for  i, j in zip(xCoords, yCoords):
                x, y = top[0] + i, top[1] + j
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                    queue.append((x, y, count+1))
                    grid[x][y] = -1

        return -1


sol = Solution()            
print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(sol.shortestPathBinaryMatrix([[0,1],[1,1]]))
print(sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
print(sol.shortestPathBinaryMatrix([[0]]))
print(sol.shortestPathBinaryMatrix([[1]]))


"""
My other solution:

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        if grid[0][0] == 1:
            return -1

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1), (i-1,j-1), (i-1,j+1), (i+1,j+1), (i+1,j-1)):
                if 0 <= x < rows and 0 <= y < cols:
                    yield x, y

        def bfs(queue):
            while queue:
                i, j, dist = queue.pop(0)
                if i == rows-1 and j == cols-1:
                    return dist
                
                for x, y in neighbors(i, j):
                    if grid[x][y] == 0 and (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y, dist+1))
            
            return -1
        
        queue = [(0, 0, 1)]
        return bfs(queue)
"""

"""
Lettcode solution using A* algorithm:
https://leetcode.com/problems/shortest-path-in-binary-matrix/solution/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Helper function for the A* heuristic.
        def best_case_estimate(row, col):
            return max(max_row - row, max_col - col)
            
        # Check that the first and last cells are open. 
        if grid[0][0] or grid[max_row][max_col]:
            return -1
        
        # Set up the A* search.
        visited = set()
        # Entries on the priority queue are of the form
        # (total distance estimate, distance so far, (cell row, cell col))
        priority_queue = [(1 + best_case_estimate(0, 0), 1, (0, 0))]
        while priority_queue:
            estimate, distance, cell = heapq.heappop(priority_queue)
            if cell in visited:
                continue
            if cell == (max_row, max_col):
                return distance
            visited.add(cell)
            for neighbour in get_neighbours(*cell):
                # The check here isn't necessary for correctness, but it
                # leads to a substantial performance gain.
                if neighbour in visited:
                    continue
                estimate = best_case_estimate(*neighbour) + distance + 1
                entry = (estimate, distance + 1, neighbour)
                heapq.heappush(priority_queue, entry)
        
        # There was no path.
        return -1
"""
