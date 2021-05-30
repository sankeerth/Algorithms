"""
1057. Campus Bikes

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 
2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) 
pair with the shortest Manhattan distance between each other, and assign the bike to that worker. 
(If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair 
with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). 
We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to

Example 1:
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

Example 2:
Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].

Note:
0 <= workers[i][j], bikes[i][j] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 1000
"""
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances, res = [], [-1] * len(workers)
        
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                distances.append((abs(wx-bx) + abs(wy-by), i, j))

        distances.sort(key=lambda x: (x[0], x[1], x[2])) # sort by distance, worker index and bike index
        assignedWorkers, assignedBikes = set(), set()

        for _, worker, bike in distances:
            if worker not in assignedWorkers and bike not in assignedBikes:
                res[worker] = bike
                assignedWorkers.add(worker)
                assignedBikes.add(bike)

                if len(assignedWorkers) == len(workers):
                    break
        
        return res


sol = Solution()
print(sol.assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))
print(sol.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))
print(sol.assignBikes([[0,0],[1,1],[2,1],[3,4]], [[6,6],[7,7],[8,8],[7,9],[7,10],[9,10]]))


"""
Leetcode discuss solution using Heap (** A very elegant solution similar to the sorted matrix problem **)

For each worker, create a sorted list of distances to each bike. The elements of the list are tuples (distance, worker, bike).
For each worker, add the tuple with the shortest distance to the heap.
Until each worker has a bike, pop the smallest distance from the heap.
If this bike is not used, update the result for this worker, else add the next closest tuple for this worker to the heap.

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []     # distances[worker] is tuple of (distance, worker, bike) for each bike 
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse = True)  # reverse so we can pop the smallest distance
        
        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
        heapq.heapify(queue)
        
        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike
        
        return result
"""

"""
Leetcode discuss solution that uses Bucket Sort (a very good thought for such use case):

Since the range of distance is [0, 2000] which is much lower than the # of pairs, which is 1e6. It's a good time to use bucket sort. Basically, it's to put each pair into the bucket representing its distance. Eventually, we can loop thru each bucket from lower distance.
Therefore, it's O(M * N) time and O(M * N) space. Only takes 60 ms in C++ beat most submissions.

class Solution {
public:
    // bucket sort
    // O(N*M) time, O(N*M) space
    vector<int> assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        // bucket sort since range of distance is [0, 2000]
        vector<vector<pair<int, int>>> buckets(2001); // buckets[i] is the vector<worker id, bike id> with distance i
        int n = workers.size(), m = bikes.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int dis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
                buckets[dis].push_back({i, j});
            }
        }
        vector<int> res(n, -1);
        vector<bool> bikeUsed(m, false);
        for (int d = 0; d <= 2000; d++) {
            for (int k = 0; k < buckets[d].size(); k++) {
                if (res[buckets[d][k].first] == -1 && !bikeUsed[buckets[d][k].second]) {
                    bikeUsed[buckets[d][k].second] = true;
                    res[buckets[d][k].first] = buckets[d][k].second;
                }
            }
        }
        return res;
    }
};
"""
