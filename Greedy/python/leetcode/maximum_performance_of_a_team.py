"""
1383. Maximum Performance of a Team

You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. 
speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72

Constraints:
1 <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        total, res = 0, 0
        speedAndEfficiency = [(s, e) for s, e in zip(speed, efficiency)]
        speedAndEfficiency.sort(key=lambda x: (-x[1], -x[0]))
        heap = []
        
        for s, e in speedAndEfficiency:
            if len(heap) > k-1:
                top = heappop(heap)
                total -= top
            
            total += s
            heappush(heap, s)
            res = max(res, (total * e))

        return res % (10 ** 9 + 7)


sol = Solution()
print(sol.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
print(sol.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))
print(sol.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4))


"""
Complexity Analysis

Let N be the total number of candidates, and KK be the size of the team.
Time Complexity: O(N⋅(logN + logK))

First of all, we build a list of candidates from the inputs, which takes O(N)O(N) time.
We then sort the candidates, which takes O(NlogN) time.
We iterate through the sorted candidates. At each iteration, we will perform at most two operations on the priority queue: one push and one pop. 
Each operation takes O(log(K−1)) time, where K−1 is the capacity of the queue. To sum up, the time complexity of this iteration will be O(N⋅log(K−1))=O(N⋅logK).
Thus, the overall time complexity of the algorithm will be O\big(N \cdot (\log N + \log K)\big)O(N⋅(logN+logK)).

Space Complexity: O(N + K)

We build a list of candidates from the inputs, which takes O(N) space.
We also use the priority queue data structure whose space capacity is O(K−1).
Note that we use sorting in the algorithm, and the space complexity of the sorting algorithm depends on the implementation of each programming language. 
For instance, the sorted() function in Python is implemented with the Timsort algorithm whose space complexity is O(N). 
While in Java, the Collections.sort() is implemented as a variant of the quicksort algorithm whose space complexity is O(logN).
To sum up, the overall space complexity of the entire algorithm is O(N + K).
"""
