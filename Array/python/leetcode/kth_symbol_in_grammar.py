"""
779. K-th Symbol in Grammar

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. 
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:
Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01

Example 3:
Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01

Example 4:
Input: n = 3, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01
row 3: 0110

Constraints:
N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""
from math import ceil


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K < 1 or K > 2**(N-1):
            return -1

        def kthGrammarRecursive(N, K):
            if N == 1:
                return '0'
            binary = kthGrammarRecursive(N-1, ceil(K/2))
            index = 1 if K % 2 == 0 else 0
            if binary == '0':
                return '01'[index]
            else:
                return '10'[index] 

        return kthGrammarRecursive(N, K)


s = Solution()
print(s.kthGrammar(4, 4))
print(s.kthGrammar(5, 11))
print(s.kthGrammar(5, 14))
print(s.kthGrammar(6, 21))
print(s.kthGrammar(6, 30))
print(s.kthGrammar(6, 17))
print(s.kthGrammar(30, 434991989))


"""
Another variant of O(log n) solution:

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K < 1 or K > 2 ** (N-1):
            return -1

        def kthGrammarRecursive(K):
            ret = -1
            if K == 1:
                ret = 0
            else:
                res = kthGrammarRecursive(int(ceil(K/2)))
                if res == 1:
                    if K % 2 == 0:
                        ret = 0
                    else:
                        ret = 1
                elif res == 0:
                    if K % 2 == 0:
                        ret = 1
                    else:
                        ret = 0

            return ret
        return kthGrammarRecursive(K)
"""

"""
My optimized but exponential solution which timed out as expected:

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K > 2**(N-1):
            return -1

        initial = ['0', '01', '0110']
        if N <= 3:
            return initial[N-1][K-1]

        string = '6'
        for i in range(4, N+1):
            temp = []
            for j in string:
                if j == '6':
                    temp.append('69')
                else:
                    temp.append('96')
            string = ''.join(temp)

        digit = string[int((K-1)/4)]
        index = ((K % 4) + 4) % 4 - 1
        if digit == '6':
            return '0110'[index]
        else:
            return '1001'[index]
"""
