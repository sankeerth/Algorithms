"""
934. Shortest Bridge

In a given 2D binary array A, there are two islands. 
(An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: A = [[0,1],[1,0]]
Output: 1

Example 2:
Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
    2 <= grid.length == grid[0].length <= 100
    grid[i][j] == 0 or grid[i][j] == 1
"""
from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        islands = []
        islandA, islandB = set(), set()

        def dfs(i, j, island):
            A[i][j] = 'X'
            island.add((i, j))

            if i-1 >= 0 and A[i-1][j] == 1:
                dfs(i-1, j, island)
            if j+1 < cols and A[i][j+1] == 1:
                dfs(i, j+1, island)
            if i+1 < rows and A[i+1][j] == 1:
                dfs(i+1, j, island)
            if j-1 >=0 and A[i][j-1] == 1:
                dfs(i, j-1, island)

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    island = set()
                    dfs(i, j, island)
                    islands.append(island)

        # island A always the smaller one as an optimization
        if len(islands[0]) < len(islands[1]):
            islandA = islands[0]
            islandB = islands[1]
        else:
            islandA = islands[1]
            islandB = islands[0]

        # Perform a BFS on the island on smaller size until a point in the larger island is found
        # Increment the distance of each append of neighbors of a point by 1 to find the distance
        # or numbers of 0s -> 1s to reach the other
        queue = [(point[0], point[1], 0) for point in islandA]
        while queue:
            item = queue.pop(0)
            i, j, distance = item[0], item[1], item[2]
            for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in islandA: # not an adjacent point in island A
                    if (x, y) in islandB:
                        return distance
                    queue.append((x, y, distance+1))
                    # Important to add the adjacent 0s to islandA so these are not added to queue again and traversed wastefully
                    islandA.add((x, y))


s = Solution()
print(s.shortestBridge([[0,1],[1,0]]))
print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
print(s.shortestBridge([[0,0,0,1,1],[0,0,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[0,0,0,1,1]]))
print(s.shortestBridge([[0,0,0,1,1],[0,0,0,1,1],[1,1,0,0,1],[1,1,0,1,1],[0,0,0,1,1]]))
print(s.shortestBridge([[0,0,0,1,1],[0,0,0,1,1],[1,1,0,0,1],[1,1,0,0,1],[0,0,0,1,1]]))


"""
My other solution:
There is no need to get the coordinates of both islands. First island (smaller or larger) is enough to be in the
visited set. The first time another island(1) is found using points from first island, result is retured.

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        visited = set()

        def neighbors(i, j):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                    yield x, y

        def bfs(queue, bridge):
            while queue:
                i, j, dist = queue.pop(0)
                for x, y in neighbors(i, j):
                    if not bridge:
                        if A[x][y] == 1:
                            queue.append((x, y, 0))
                            visited.add((x, y))
                    else:
                        if A[x][y] == 1:
                            return dist
                        queue.append((x, y, dist+1))
                        visited.add((x, y))
                    

        for i in range(rows):
            found = False
            for j in range(cols):
                if A[i][j] == 1:
                    visited.add((i, j))
                    bfs([(i, j, 0)], False)
                    found = True
                    break
            if found:
                break

        queue = [(i, j, 0) for i, j in visited]
        res = bfs(queue, True)
        return res
"""
