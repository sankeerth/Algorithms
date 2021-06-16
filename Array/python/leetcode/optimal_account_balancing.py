"""
465. Optimal Account Balancing

You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] 
indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.
Return the minimum number of transactions required to settle the debt.

Example 1:
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:
Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

Constraints:

1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi <= 20
fromi != toi
1 <= amounti <= 100
"""
from typing import List
from collections import defaultdict


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        amountOwed = defaultdict(int)

        for a, b, amt in transactions:
            amountOwed[a] += amt
            amountOwed[b] -= amt

        amounts = [x for x in amountOwed.values() if x != 0]
        
        def minTransfersRecursive(i):
            while i < len(amounts) and amounts[i] == 0:
                i += 1
            
            if i == len(amounts):
                return 0

            res = float('inf')
            for j in range(i+1, len(amounts)):
                if amounts[i] * amounts[j] < 0:
                    amounts[j] += amounts[i]
                    res = min(res, minTransfersRecursive(i+1) + 1) # should be i+1 and not j
                    amounts[j] -= amounts[i]

            return res

        return minTransfersRecursive(0)


sol = Solution()
print(sol.minTransfers([[0,1,10],[2,0,5]]))
print(sol.minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]]))
print(sol.minTransfers([[0,1,1],[1,2,1],[2,3,4],[3,4,5]]))


"""
Leetcode discuss posts:
https://leetcode.com/problems/optimal-account-balancing/discuss/95355/Concise-9ms-DFS-solution-(detailed-explanation)
https://leetcode.com/problems/optimal-account-balancing/discuss/95365/Easy-java-solution-with-explanation
"""
