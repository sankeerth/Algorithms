"""
1526. Minimum Number of Increments on Subarrays to Form a Target Array

Given an array of positive integers target and an array initial of same size with all zeros.
Return the minimum number of operations to form a target array from initial if you are allowed to do the following operation:
Choose any subarray from initial and increment each value by one.
The answer is guaranteed to fit within the range of a 32-bit signed integer.

Example 1:
Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.

Example 2:
Input: target = [3,1,1,2]
Output: 4
Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).

Example 3:
Input: target = [3,1,5,4,2]
Output: 7
Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).
Example 4:
Input: target = [1,1,1,1]
Output: 1

Constraints:
1 <= target.length <= 10^5
1 <= target[i] <= 10^5
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    # My O(N logN) solution
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        heap, initial = [], [0] * len(target)
        for i, num in enumerate(target):
            heappush(heap, (num, i))
        
        def populate(index, increment):
            i, j = index-1, index+1
            while i >= 0 and initial[i] + increment <= target[i]:
                initial[i] += increment
                i -= 1
            
            while j < len(target) and initial[j] + increment <= target[j]:
                initial[j] += increment
                j += 1
        
        while heap:
            num, index = heappop(heap)
            if initial[index] < target[index]:
                increment = target[index] - initial[index]
                initial[index] += increment
                populate(index, increment)
                res += increment
            
        return res      


sol = Solution()
print(sol.minNumberOperations([1,2,3,2,1]))
print(sol.minNumberOperations([3,1,1,2]))
print(sol.minNumberOperations([3,1,5,4,2]))
print(sol.minNumberOperations([1,1,1,1]))


"""
Leetcode discuss solution: O(N)
Explanation: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/754623/Detailed-Explanation

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res, reuse = target[0], target[0]
        for i in range(1, len(target)):
            if target[i] <= reuse:
                reuse = target[i]
            else:
                res += target[i] - reuse
                reuse = target[i]

        return res

Refactored:

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                res += target[i] - target[i-1]

        return res        
"""
