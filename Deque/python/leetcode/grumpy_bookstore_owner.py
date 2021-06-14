"""
1052. Grumpy Bookstore Owner

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, 
and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0. 
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes minutes straight, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day. 

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Note:
1 <= minutes <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        withoutGrumpy, satisfiedCustomers = 0, 0
        
        for i in range(len(customers)):
            if not grumpy[i]:
                satisfiedCustomers += customers[i]

        for i in range(minutes):
            if grumpy[i]:
                withoutGrumpy += customers[i]

        res = satisfiedCustomers + withoutGrumpy
        i, j = 0, minutes
        while j < len(customers):
            if grumpy[i]:
                withoutGrumpy -= customers[i]
            if grumpy[j]:
                withoutGrumpy += customers[j]
            
            res = max(res, satisfiedCustomers + withoutGrumpy)
            i += 1
            j += 1

        return res


sol = Solution()
print(sol.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))


"""
Leetcode discuss solution:

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        # Part 1 requires counting how many customers
        # are already satisfied, and removing them
        # from the customer list.
        already_satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0: #He's happy
                already_satisfied += customers[i]
                customers[i] = 0
        
        # Part 2 requires finding the optinal number
        # of unhappy customers we can make happy.
        best_we_can_make_satisfied = 0
        current_satisfied = 0
        for i, customers_at_time in enumerate(customers):
            current_satisfied += customers_at_time # Add current to rolling total
            if i >= minutes: # We need to remove some from the rolling total
                current_satisfied -= customers[i - minutes]
            best_we_can_make_satisfied = max(best_we_can_make_satisfied, current_satisfied)
        
        # The answer is the sum of the solutions for the 2 parts.
        return already_satisfied + best_we_can_make_satisfied
"""
