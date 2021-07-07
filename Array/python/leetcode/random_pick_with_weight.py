"""
528. Random Pick with Weight

You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. 
pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], 
the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
More formally, the probability of picking index i is w[i] / sum(w).

Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]
Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.
Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.

Constraints:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
"""
from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = [0] * (len(w)+1)
        for i in range(len(w)):
            self.prefixSum[i+1] = self.prefixSum[i] + w[i]
        
        self.start = 0
        self.end = self.prefixSum[-1]-1
        self.length = len(w)

    def pickIndex(self) -> int:
        # binary search for closest prev value
        target = random.randint(self.start, self.end)
        lo, hi = 0, self.length
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.prefixSum[mid] <= target < self.prefixSum[mid+1]:
                return mid
            elif target > self.prefixSum[mid]:
                lo = mid
            else:
                hi = mid
        return lo


def execute(cmds, inputs):
    sol = None
    res = []
    
    for cmd, input in zip(cmds, inputs):
        if cmd == 'Solution':
            sol = Solution(input[0])
            ret = None
        elif cmd == 'pickIndex':
            ret = sol.pickIndex()

        res.append(ret)
    return res


cmds = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
inputs = [[[1,3]],[],[],[],[],[]]
print(execute(cmds, inputs))

"""
Leetcode solution of binary search for closest previous value

def pickIndex(self) -> int:
    target = self.total_sum * random.random()
    # run a binary search to find the target zone
    low, high = 0, len(self.prefix_sums)
    while low < high:
        mid = low + (high - low) // 2
        if target > self.prefix_sums[mid]:
            low = mid + 1
        else:
            high = mid
    return low
"""
