"""
675. Cut Off Trees for Golf Event
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. 
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. 
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6

Example 2:
Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1

Example 3:
Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
"""
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest:
            return 0

        rows, cols = len(forest), len(forest[0])
        trees_position = [(forest[i][j], i, j) for i in range(rows) for j in range(cols) if forest[i][j] > 1]
        trees_position = sorted(trees_position, key=lambda x: x[0])
        trees_position.insert(0, (forest[0][0], 0, 0))  # insert the start index irrespective of whether it is already there or not. if it is already there then the distance would just be 0

        def neighbors(i, j, visited):
            for x, y in ((i-1,j), (i,j+1), (i+1,j), (i,j-1)):
                if 0 <= x < rows and 0 <= y < cols and forest[x][y] > 0 and (x, y) not in visited:
                    yield x, y


        res = 0
        def bfs(src, dest):
            _, i, j = src
            queue = [(i, j)]
            visited = set()
            visited.add((i, j))
            distance = 0

            while queue:
                length = len(queue)
                for _ in range(length):
                    i, j = queue.pop(0)
                    # visited.add((i, j))  # see the below comment
                    if i == dest[1] and j == dest[2]:
                        forest[i][j] = 1
                        return distance
                    
                    for x, y in neighbors(i, j, visited):
                            queue.append((x, y))
                            visited.add((x, y))  # this was added at the place commented above. That would just add duplicate trees into the queue for processing and would increase time by a loooot!
                distance += 1

            return -1

        for pos in range(len(trees_position)-1):
            src = trees_position[pos]
            dest = trees_position[pos+1]

            d = bfs(src, dest)
            if d == -1:
                return -1
            else:
                res += d

        return res


sol = Solution()
print(sol.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
print(sol.cutOffTree([[0, 2, 3], [0, 0, 4], [7, 6, 5]]))
print(sol.cutOffTree([[0, 0, 3], [0, 0, 4], [7, 6, 5]]))
print(sol.cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]]))
print(sol.cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]]))
print(sol.cutOffTree([[2, 3, 4], [0, 0, 5], [6, 7, 8]]))
print(sol.cutOffTree([]))
print(sol.cutOffTree([[0, 1, 1]]))
print(sol.cutOffTree([[54581641, 64080174, 24346381, 69107959], [86374198, 61363882, 68783324, 79706116], [668150, 92178815, 89819108, 94701471], [83920491, 22724204, 46281641, 47531096], [89078499, 18904913, 25462145, 60813308]]))


"""
Leetcode discuss solution using Hadlock's algorithm:
https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/107396/Python-solution-based-on-wufangjie's-(Hadlock's-algorithm)

Just my own very similar implementation of @wufangjie's solution (and some terminology from the Hadlock algorithm which @awice mentioned to me), 
with some more explanation. Gets accepted in about 700 ms.

Basically find the trees, sort them by order, find the distance from each tree to the next, and sum those distances. But how to find the distance from one cell 
to some other cell? BFS is far to slow for the current test suite. Instead use what's apparently known as "Hadlock's Algorithm" (though I've only seen high-level descriptions of that). 
First try paths with no detour (only try steps in the direction towards the goal), then if necessary try paths with one detour step, then paths with two detour steps, etc. 
The distance then is the Manhattan distance plus twice the number of detour steps (twice because you'll have to make up for a detour step with a later step back towards the goal).

How to implement that?

Round 1: Run a DFS only on cells that you can reach from the start cell with no detour towards the goal, i.e., 
only walking in the direction towards the goal. If this reaches the goal, we're done. Otherwise...
Round 2: Try again, but this time try starting from all those cells reachable with one detour step. Collect these in round 1.
Round 3: If round 2 fails, try again but start from all those cells reachable with two detour steps. Collect these in round 2.
And so on...
If there are no obstacles, then this directly walks a shortest path towards the goal, which is of course very fast. 
Much better than BFS which would waste time looking in all directions. With only a few obstacles, it's still close to optimal.

My distance function does this searching algorithm. I keep the current to-be-searched cells in my now stack. 
When I move to a neighbor that's closer to the goal, I also put it in now. If it's not closer, then that's a detour step so 
I just remember it on my soon stack for the next round.

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                for i, row in enumerate(forest)
                for j, height in enumerate(row)
                if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def distance(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i+1, j, i < I), (i-1, j, i > I), (i, j+1, j < J), (i, j-1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))

        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))
"""
