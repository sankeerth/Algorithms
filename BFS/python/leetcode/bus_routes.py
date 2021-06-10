"""
815. Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. 
For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels 
in the sequence 1->5->7->1->5->7->1->... forever.
We start at bus stop S (initially not on a bus), and we want to go to bus stop T. 
Travelling by buses only, what is the least number of buses we must take to reach our destination? 
Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
"""
from typing import List
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        busRoutes = defaultdict(set)
        for routeNum, route in enumerate(routes):
            for bus in route:
                busRoutes[bus].add(routeNum)

        queue, seenRoutes, seenBuses = list(), set(), set()
        queue.append((0, S))
        seenBuses.add(S)

        while queue:
            stops, bus = queue.pop(0)
            if bus == T:
                return stops

            for route in busRoutes[bus]:
                if route not in seenRoutes:
                    seenRoutes.add(route)
                    for busStop in routes[route]:
                        # This is not really needed but good to have. Else it will add the same bus again but as the route will be marked as seen,
                        # stops in the same route will not be traversed. So an extra pop and check for seenRoutes.
                        # Tested removing the seenBuses set and printing the len(queue) after each iteration for the TLE testcase.
                        # Indeed the bus get again to the queue
                        if busStop not in seenBuses:
                            seenBuses.add(busStop)
                            queue.append((stops+1, busStop))
                
        return -1


s = Solution()
print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 1))
print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 7))
print(s.numBusesToDestination([[1,2,5],[3,6,7]], 1, 7))
print(s.numBusesToDestination([[1,2,5],[3,6,7],[4,5]], 1, 7))
print(s.numBusesToDestination([[1,2,5],[3,6,7],[3,4,5]], 1, 7))


"""
Inital solution times out for a very large test case since the bus route is traversed again.
Even though the buses in the route are added to visited, traversing the route again has a cost.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        busRoutes = defaultdict(set)
        for route in routes:
            for bus in route:
                for r in route:
                    if bus != r:
                        busRoutes[bus].add(r)

        queue, visited = list(), set()
        queue.append((0, S))
        visited.add(S)

        while queue:
            count, bus = queue.pop(0)
            if bus == T:
                return count

            if T in busRoutes[bus]:
                return count+1

            for route in busRoutes[bus]:
                if route not in visited:
                    visited.add(route)
                    queue.append((count+1, route))
                
        return -1
"""
