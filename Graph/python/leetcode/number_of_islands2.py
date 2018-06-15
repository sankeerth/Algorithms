"""
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""


class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        count = 0
        result = list()
        grid = [[0] * n for _ in range(m)]
        array = [i for i in range(m * n)]
        size = [1 for _ in range(m * n)]
        x_coor = [-1, 0, 1, 0]
        y_coor = [0, -1, 0, 1]

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

        for position in positions:
            i, j = position[0], position[1]
            grid[i][j] = 1
            count += 1
            for k in range(len(x_coor)):
                x, y = i + x_coor[k], j + y_coor[k]
                if -1 < x < m and -1 < y < n and grid[x][y] == 1:
                    if union(i * n + j, x * n + y):
                        count -= 1
            result.append(count)

        return result


sol = Solution()
print(sol.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
print(sol.numIslands2(1, 2, [[0, 1], [0, 0]]))
print(sol.numIslands2(3, 3, [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1]]))
