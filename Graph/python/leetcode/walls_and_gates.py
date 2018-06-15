"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""


class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        queue = list()
        m, n = len(rooms), len(rooms[0])
        x_coor = [-1, 0, 1, 0]
        y_coor = [0, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            cur = queue.pop(0)
            i , j = cur[0], cur[1]
            val = rooms[i][j]
            for k in range(len(x_coor)):
                x, y = i + x_coor[k], j + y_coor[k]
                if -1 < x < m and -1 < y < n and rooms[x][y] != -1:
                    if rooms[x][y] == 2147483647:
                        rooms[x][y] = val + 1
                        queue.append((x, y))

        return rooms


sol = Solution()
print(sol.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))


'''
leetcode solution using BFS:
leetcode comment: I suggest that for this kind of problem using BFS instead of DFS which may lead you to a fail in the 
real interview. DFS may do a lot of duplicate operations.

public void wallsAndGates(int[][] rooms) {
    for (int i = 0; i < rooms.length; i++)
        for (int j = 0; j < rooms[0].length; j++)
            if (rooms[i][j] == 0) dfs(rooms, i, j, 0);
}

private void dfs(int[][] rooms, int i, int j, int d) {
    if (i < 0 || i >= rooms.length || j < 0 || j >= rooms[0].length || rooms[i][j] < d) return;
    rooms[i][j] = d;
    dfs(rooms, i - 1, j, d + 1);
    dfs(rooms, i + 1, j, d + 1);
    dfs(rooms, i, j - 1, d + 1);
    dfs(rooms, i, j + 1, d + 1);
}

'''