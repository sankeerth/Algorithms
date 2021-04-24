"""
1029. Two City Scheduling

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city. 

Example 1:
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Example 3:
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
"""
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost = 0
        costs.sort(key=lambda x: x[0]-x[1])
        
        for i in range(len(costs)//2):
            totalCost += costs[i][0] + costs[len(costs)-1-i][1]

        return totalCost


s = Solution()
print(s.twoCitySchedCost([[10,20],[20,30]]))
print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[20,190]]))
print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
print(s.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))

"""
Using functools and custom compare function:

from functools import cmp_to_key

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost = 0
        def compare(a, b):
            if (a[1]-a[0]) < (b[1]-b[0]):
                return 1
            elif (a[1]-a[0]) > (b[1]-b[0]):
                return -1
            else:
                if a[0] < b[0]:
                    return -1
                else:
                    return 1
        
        cmp = cmp_to_key(compare)
        costs.sort(key=cmp)
        print(costs)

        for i in range(len(costs)//2):
            totalCost += costs[i][0] + costs[len(costs)-1-i][1]

        return totalCost
"""
