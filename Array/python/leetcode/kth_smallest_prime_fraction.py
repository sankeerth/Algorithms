"""
786. K-th Smallest Prime Fraction

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:
Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:
2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lastIndex = len(arr)-1
        i, j = 0, len(arr)-1
        heap = []
        heappush(heap, (arr[i]/arr[j], i, j))

        smallest = 1
        while heap:
            _, i, j = heappop(heap)
            if smallest == k:
                break
            
            if j-1 > i:
                heappush(heap, (arr[i]/arr[j-1], i, j-1))

            if j == lastIndex and i+1 <= lastIndex:
                heappush(heap, (arr[i+1]/arr[j], i+1, j))
            
            smallest += 1

        return [arr[i], arr[j]]


sol = Solution()
print(sol.kthSmallestPrimeFraction([1,2,3,5], 3))
print(sol.kthSmallestPrimeFraction([1,2,3,5], 5))
print(sol.kthSmallestPrimeFraction([1,2,3,5,7,11,13,17], 6))
print(sol.kthSmallestPrimeFraction([1,2,3,5,7,11,13,17], 11))
print(sol.kthSmallestPrimeFraction([1,2,3,5,7,11,13,17], 14))
print(sol.kthSmallestPrimeFraction([1,2,3,5,7,11,13,17], 27))


"""
Leetcode solution using binary search:

Intuition
Let under(x) be the number of fractions below x. It's an increasing function on x, so we can binary search for the correct answer.

Algorithm
Let's binary search for x such that there are exactly K fractions below x. At the same time, we'll record the largest such fraction 
seen that was still below x.
Our binary search follows a similar template as other binary searches: we have some interval [lo, hi] and a midpoint mi = (lo + hi) / 2.0. 
If the number of fractions below mi is less than K, then we will now consider the interval [mi, hi]; otherwise we will consider the interval [lo, mi]. 
Our under(x) function has two objectives: to return the number of fractions below x, as well as the maximum such fraction below x. 
To count this, we will use a sliding window approach: for each primes[j], we'll find the largest i so that primes[i] / primes[j] < x. 
These is are necessarily increasing as j (and primes[j]) increases, so this check is linear.


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def binarySearch(fraction):
            count, maxPrimeFraction = 0, 0
            i, j = -1, 1
            res = [arr[i], arr[j]]
            while j < len(arr):
                while arr[i+1] < arr[j] * fraction:
                    i += 1
                count += i+1
                if i >= 0 and arr[i]/arr[j] > maxPrimeFraction:
                    maxPrimeFraction = arr[i]/arr[j]
                    res = [arr[i], arr[j]]
                j += 1

            return count, res

        lo, hi = 0.0, 1.0
        res = [arr[0], arr[-1]]
        while hi - lo > 1e-9:
            mi = (lo + hi) / 2.0
            count, maxPrimeFraction = binarySearch(mi)
            if count < k:
                lo = mi
            else:
                res = maxPrimeFraction
                hi = mi

        return res
"""
