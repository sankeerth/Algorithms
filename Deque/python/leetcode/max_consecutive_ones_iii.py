"""
1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""
from typing import List
from collections import deque


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        result = 0 
        i, j, zeros = 0, 0, 0
        dq = deque()

        while j < len(A):
            if A[j] == 0:
                dq.append(j)
                zeros += 1
                if zeros > K:
                    i = dq.popleft() + 1
            
            result = max(result, j-i+1)
            j += 1
        
        return result


s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(s.longestOnes([0,0,1,1,1,0,0,0,1,1,1,1,0], 2))
print(s.longestOnes([0,0,0,1,1,1,0,0,0,1,1,1,1,0], 2))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))


"""
My solution using two pointers:

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, j, res = 0, 0, 0
        count = 0

        while j < len(A):
            if A[j] == 0:
                count += 1
                while count > K and i <= j:
                    if A[i] == 0:
                        count -= 1
                    i += 1
            
            res = max(res, j-i+1)
            j += 1

        return res
"""
