"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

import math


class Solution(object):
    # Catalan Number  (2n)!/((n+1)!*n!)
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))

    # DP
    def numTrees1(self, n):
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]


sol = Solution()
print(sol.numTrees1(2))
print(sol.numTrees1(3))
print(sol.numTrees1(4))
print(sol.numTrees1(5))

"""
My solution:

class Solution:
    def numTrees(self, n: int) -> int:
        res = {0:1, 1:1, 2:2, 3:5}
        
        def numTreesRec(n):
            if n in res:
                return res[n]
            
            count = 0
            for i in range(n):
                l = numTreesRec(i)
                r = numTreesRec(n-i-1)
                count += l*r
            
            res[n] = count
            return count

        return numTreesRec(n)
"""
