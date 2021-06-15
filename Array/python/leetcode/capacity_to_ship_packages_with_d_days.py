"""
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)

        def getRequiredDays(maxCapacity):
            capacity, days = 0, 1
            for weight in weights:
                capacity += weight
                if capacity > maxCapacity:
                    days += 1
                    capacity = weight
            return days

        while lo < hi:
            capacity = (lo + hi) // 2
            requiredDays = getRequiredDays(capacity)

            if requiredDays > days:
                lo = capacity + 1
            else:
                hi = capacity
        
        return hi


sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(sol.shipWithinDays([1,2,3,4,5], 3))
print(sol.shipWithinDays([1,2,3,1,1], 4))
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 10))
print(sol.shipWithinDays([68,25,170,494,202,88,151,296,329,365,417,81,441,366,230,408,240,356,253,489,137,209], 11)) # failing test case


"""
Explanation of this solution:

The key is left = max(weights), right = sum(weights),
which are the minimum and maximum possible weight capacity of the ship.

Therefore the question becomes Binary Search to find the minimum weight capacity of the ship between left and right.
We start from
mid = (left + right) / 2 as our current weight capacity of the ship.
need = days needed == 1
cur = current cargo in the ship == 0

Start put cargo into ship in order.
when need > D, it means the current ship is too small, we modify left = mid + 1 and continue
If all the cargo is successfully put into ships, we might have a chance to find a smaller ship, so let right = mid and continue.
Finally, when our left == right, we reach our answer
"""

"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search

Given the number of bags,
return the minimum capacity of each bag,
so that we can put items one by one into all bags.

We binary search the final result.
The left bound is max(A),
The right bound is sum(A).


Here are some similar binary search problems:

1482. Minimum Number of Days to Make m Bouquets
1283. Find the Smallest Divisor Given a Threshold
1231. Divide Chocolate
1011. Capacity To Ship Packages In N Days
875. Koko Eating Bananas
774. Minimize Max Distance to Gas Station
410. Split Array Largest Sum
"""

"""
My DP recursive solution that gives TLE:

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        weightSum = sum(weights)
        minCapacity = ceil(weightSum / days)
        prefixSum = [0] * (len(weights)+1)
        dp = {}
        for i in range(1, len(weights)+1):
            prefixSum[i] = prefixSum[i-1] + weights[i-1]

        def shipWithinDaysRecursive(i, days):
            if days == 1:
                return prefixSum[len(weights)] - prefixSum[i]
            
            if (i, days) in dp:
                return dp[(i, days)]

            res = float('inf')
            for j in range(i+1, len(weights)-days+2):
                capacity = prefixSum[j] - prefixSum[i]
                if capacity <= minCapacity * 2:
                    ret = shipWithinDaysRecursive(j, days-1)
                    res = min(res, (max(capacity, ret)))

            dp[(i, days)] = res
            return res

        res = shipWithinDaysRecursive(0, days)
        return res if res != float('inf') else max(weights)
"""
