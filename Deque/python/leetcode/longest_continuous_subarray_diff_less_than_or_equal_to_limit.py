"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest 
non-empty subarray such that the absolute difference between any two elements of this 
subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
from typing import List
import heapq


class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val


class Solution:
    # Complexity: O(N logN)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start, result = 0, 0
        minHeap = MinHeap()
        maxHeap = MaxHeap()

        for i, num in enumerate(nums):
            while minHeap and abs(num-minHeap[0][0]) > limit:
                start = max(start, minHeap[0][1] + 1)
                minHeap.heappop()

            while maxHeap and abs(num-maxHeap[0][0]) > limit:
                start = max(start, maxHeap[0][1] + 1)
                maxHeap.heappop()

            minHeap.heappush((num, i))
            maxHeap.heappush((num, i))

            result = max(result, i-start+1)

        return result


s = Solution()
print(s.longestSubarray([1,3,6,2,7], 4)) # good example to debug and understand
print(s.longestSubarray([10,1,3,2,4,7,2,8], 4)) # good example to debug and understand
print(s.longestSubarray([8,2,4,11], 4))
print(s.longestSubarray([10,1,2,4,7,2], 5))
print(s.longestSubarray([4,2,2,2,4,4,2,2], 0))
print(s.longestSubarray([3], 1))
print(s.longestSubarray([6], 7))
print(s.longestSubarray([1,5,6,7,8,10,6,5,6], 4))
print(s.longestSubarray([1,1,6,5,7,8,10,6,5,6], 4))
print(s.longestSubarray([4,8,5,1,7,9], 6))
print(s.longestSubarray([1,2,3,4,5,6,7,8,9,10,11,12], 5))



"""
Leetcode discuss solution of O(N) complexity:
Decent explanation: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609743/Java-Detailed-Explanation-Sliding-Window-Deque-O(N)

Let's work on sliding window max first. By using max Deque. We maintain list of max element 
candidates in monotonically decreasing order. Everytime the right pointer reaches a new position, 
we need to dequeue the "tail" element who is smaller than the nums[right]. 
Since, those "old small tail" elements will never be the range maximum from now on. 
After "clean up" the "old small tail" elements, add nums[right] into the deque, and then, 
the head of deque is the current maximum.

Same for the min Deque. Move right poniter by 1, and clean up "old big tail" elements, 
add nums[right], the head of deque is the current minimum.

What we should do next is to shrink left pointer because of limit. If current.max - current.min > limit. 
We should move the left pointer. Accordingdly, we need to update our min max deques. 
If head of max deque is equal to the nums[left], that means, it is the one, we need to dequeue it, 
since we are gonna move the left pointer by 1. (Note: nums[left] will be never larger than head of max deque, 
and if nums[left] is smaller than the head, we good, keep moving left pointer until satisfying the limit).

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQ = deque()
        minQ = deque()
        l, res = 0, 0

        # find the longest subarray for every right pointer by shrinking left pointer
        for r, num in enumerate(nums):
            # update maxDeque with new right pointer
            while len(maxQ) and num > maxQ[-1]:
                maxQ.pop()
            # update minDeque with new right pointer
            while len(minQ) and num < minQ[-1]:
                minQ.pop()

            maxQ.append(num)
            minQ.append(num)

            # shrink left pointer if exceed limit
            while maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[l]: 
                    maxQ.popleft()
                if minQ[0] == nums[l]: 
                    minQ.popleft()
                l += 1 # shrink it

            # update res
            res = max(res, r-l+1)
        
        return res
"""

"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)

More Similar Sliding Window Problems

1425. Constrained Subsequence Sum
1358. Number of Substrings Containing All Three Characters
1248. Count Number of Nice Subarrays
1234. Replace the Substring for Balanced String
1004. Max Consecutive Ones III
930. Binary Subarrays With Sum
992. Subarrays with K Different Integers
904. Fruit Into Baskets
862. Shortest Subarray with Sum at Least K
209. Minimum Size Subarray Sum

More Good Stack Problems
Here are some stack problems that impressed me.

1425. Constrained Subsequence Sum
1130. Minimum Cost Tree From Leaf Values
907. Sum of Subarray Minimums
901. Online Stock Span
856. Score of Parentheses
503. Next Greater Element II
496. Next Greater Element I
84. Largest Rectangle in Histogram
42. Trapping Rain Water
"""

"""
My Solution:
Time limit exceeded for last case. For a case like: [1,2,3,4,5,6,7,8,9,10,11,12], 5
Needs to go until 7 and then back to 2
Next to 8 and back to 3
Therefore time complexity is still O(n^2)

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start, result = 0, 0
        min_, max_ = nums[0], nums[0]

        for i, current in enumerate(nums):
            if abs(current-min_) > limit or abs(max_-current) > limit:
                j = i
                min_, max_ = current, current
                while abs(current-nums[j]) <= limit:
                    j -= 1
                    min_ = min(min_, nums[j])
                    max_ = max(max_, nums[j])
                start = j+1
            
            min_ = min(min_, current)
            max_ = max(max_, current)
            result = max(result, i-start+1)                    

        return result 
"""
