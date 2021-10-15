"""
787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:
The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
from typing import List
from collections import defaultdict


# Check Solution page in Leetcode. It is very good and has 4 approaches: Djiktras, Bellman, DFS with memo and BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        memo = {}
        memo[dst] = 0
        graph = defaultdict(list)

        for flight in flights:
            start, end, cost = flight
            graph[start].append((end, cost))

        def dfs(start, stops):
            if start == dst:
                return 0
            if stops < 0:
                return float('inf')
            
            if (start, stops) in memo:
                return memo[(start, stops)]

            cost = float('inf')
            for nxt, c in graph[start]:
                cost = min(cost, dfs(nxt, stops-1) + c)
            
            memo[(start, stops)] = cost
            return cost

        cost = dfs(src, K)
        return -1 if cost == float('inf') else cost
        

sol = Solution()
print(sol.findCheapestPrice(15, [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]], 1, 4, 10))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
print(sol.findCheapestPrice(3, [[0,1,50],[1,2,10],[2,3,25],[3,4,25],[2,5,5],[1,5,25],[0,5,100],[5,4,75]], 0, 4, 0))
print(sol.findCheapestPrice(3, [[0,1,50],[1,2,10],[2,3,25],[3,4,25],[2,5,5],[1,5,25],[0,5,100],[5,4,75]], 0, 4, 1))
print(sol.findCheapestPrice(3, [[0,1,50],[1,2,10],[2,3,25],[3,4,25],[2,5,5],[1,5,25],[0,5,100],[5,4,75]], 0, 4, 2))
print(sol.findCheapestPrice(3, [[0,1,50],[1,2,10],[2,3,25],[3,4,25],[2,5,5],[1,5,25],[0,5,100],[5,4,75]], 0, 4, 3))
print(sol.findCheapestPrice(3, [[0,1,50],[1,2,10],[2,3,25],[3,4,75],[2,5,5],[1,5,25],[0,5,100],[5,4,75]], 0, 4, 4))


"""
BFS solution timing out:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        res, stops = float('inf'), 0
        queue = []
        graph = defaultdict(list)

        for flight in flights:
            start, end, cost = flight
            graph[start].append((end, cost))

        for node in graph[src]:
            queue.append(node)
        queue.append('|')

        while queue:
            if stops > K:
                break

            top = queue.pop(0)
            if top == '|':
                stops += 1
                queue.append('|')
                continue

            dest, fromCost = top
            if dest == dst:
                res = min(res, fromCost)
            else:
                for to, toCost in graph[dest]:
                    item = (to, fromCost + toCost)
                    queue.append(item)

        return -1 if res == float('inf') else res
"""
