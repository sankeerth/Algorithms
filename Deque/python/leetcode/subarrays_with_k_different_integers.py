"""
992. Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the 
number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.

Example 1:
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Note:
1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""
from typing import List
from collections import defaultdict, Counter


class Window:
    def __init__(self):
        self.count = Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution(object):
    # Good explanation: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2BJava-with-picture-prefixed-sliding-window
    def subarraysWithKDistinct(self, A, K):
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for _, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans
        

sol = Solution()
print(sol.subarraysWithKDistinct([1,1,1,2], 2))
print(sol.subarraysWithKDistinct([1,2,1,2,3], 2))
print(sol.subarraysWithKDistinct([1,2,1,2], 2))
print(sol.subarraysWithKDistinct([1,1,1,2,2], 2))
print(sol.subarraysWithKDistinct([1,1,1,2,2], 1))
print(sol.subarraysWithKDistinct([1,1,1,2,2], 3))
print(sol.subarraysWithKDistinct([1,2,1,2,1,2,3,4], 2))
print(sol.subarraysWithKDistinct([1,2,1,2,1,2,3,4], 3))


"""
Template with working code for many similar sliding window/2 pointer problems:

https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!
"""

"""
Draw this out as this forms the basis for the algo in Leetcode solution. 
Complexity -> O(n) * K. The idea is to compute the first index of the window that has K distinct integers.

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        res, start, i = 0, 0, 0
        mapOfStartEndIndices = {}

        while i < len(A):
            cur = A[i]
            if cur in mapOfStartEndIndices:
                    mapOfStartEndIndices[cur][1] = i
            else:
                mapOfStartEndIndices[cur] = [i, i]

            if len(mapOfStartEndIndices) >= K:
                if len(mapOfStartEndIndices) > K:
                    itemWithLowestLastSeenIndex = min(mapOfStartEndIndices.items(), key=lambda v: v[1][1])
                    start = itemWithLowestLastSeenIndex[1][1] + 1
                    del mapOfStartEndIndices[itemWithLowestLastSeenIndex[0]]

                # len(mapOfStartEndIndices) == K
                itemWithLowestLastSeenIndex = min(mapOfStartEndIndices.items(), key=lambda v: v[1][1])
                startOfMinUniqueWindow = itemWithLowestLastSeenIndex[1][1]
                res += startOfMinUniqueWindow - start + 1

            i += 1

        return res
"""

"""
Leetcode solution: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
Complexity - O(N)

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res
"""

"""
Another Leetcode solution:

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                # remove the distinct at start_k, move start_k, start
                del freq[A[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                # update start_k and res (Notice: K >= 1)
                while freq[A[start_k]] > 1:
                    freq[A[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
        return res
"""
