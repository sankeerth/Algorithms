"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        array = [i for i in range(m * n)]
        size = [1 for _ in range(m * n)]
        x_coor = [-1, 0]
        y_coor = [0, -1]

        def root(x):
            while x != array[x]:
                x = array[x]
            return x

        def union(x, y):
            root_x = root(x)
            root_y = root(y)

            if root_x == root_y:
                return False

            if size[root_x] < size[root_y]:
                size[root_y] += size[root_x]
                array[root_x] = root_y
            else:
                size[root_x] += size[root_y]
                array[root_y] = root_x

            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    for k in range(len(x_coor)):
                        x, y = i + x_coor[k], j + y_coor[k]
                        if -1 < x < m and -1 < y < n and grid[x][y] == "1":
                            if union(i * n + j, x * n + y):
                                    result -= 1
        return result


sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(sol.numIslands([["1", "0", "1"]]))
print(sol.numIslands([["0", "1"], ["1", "1"]]))
print(sol.numIslands([[]]))


'''
My BFS solution:

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            nonlocal result, m, n
            result += 1
            queue = list()
            queue.append((i, j))

            x_coor = [-1, 0, 1, 0]
            y_coor = [0, -1, 0, 1]

            while queue:
                cur = queue.pop(0)
                visited.add((cur[0], cur[1]))
                for i in range(len(x_coor)):
                    x, y = cur[0] + x_coor[i], cur[1] + y_coor[i]
                    if -1 < x < m and -1 < y < n and (x, y) not in visited and grid[x][y] == "1":
                        visited.add((x, y))
                        queue.append((x, y))

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)

        return result
'''

'''
My DFS solution:

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        visited = set()

        x_coor = [-1, 0, 1, 0]
        y_coor = [0, -1, 0, 1]

        def dfs(i, j):
            visited.add((i, j))
            for k in range(len(x_coor)):
                x, y = i + x_coor[k], j + y_coor[k]
                if -1 < x < m and -1 < y < n:
                    if grid[x][y] == "1" and (x, y) not in visited:
                        dfs(x, y)

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    result += 1
                    dfs(i, j)

        return result
'''