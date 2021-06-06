"""
503. Next Greater Element II

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in 
the array, which means you could search circularly to find its next greater number. If it doesn't exist, 
return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        res = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                top = stack.pop()
                res[top] = nums[i]
            stack.append(i)

        while stack:
            top = stack.pop()
            if stack and nums[stack[0]] > nums[top]:
                res[top] = nums[stack[0]]

        return res[:len(nums)//2]


sol = Solution()
print(sol.nextGreaterElements([1,2,1]))
print(sol.nextGreaterElements([1,2,3,4,3]))
print(sol.nextGreaterElements([3,3,3,3]))
print(sol.nextGreaterElements([5,4,3,2,1]))
print(sol.nextGreaterElements([1,5,2,3,4,3]))
print(sol.nextGreaterElements([1,2,3,2,1])) # failed test case
print(sol.nextGreaterElements([3,8,4,1,2]))


"""
Leetcode solution using 2 passes and traversing from reverse:
Watch animation in Leetcode solution for explanation

Assume that nums[j] is the correct Next Greater Element for nums[i], such that i < j ≤ stack[top]. 
Now, whenever we encounter nums[j]nums[j], if nums[j]>nums[stack[top]], 
it would have already popped the previous stack[top] and j would have become the topmost element. 
On the other hand, if nums[j]<nums[stack[top]], it would have become the topmost element by 
being pushed above the previous stack[top]. In both the cases, if nums[j]>nums[i], 
it will be correctly determined to be the Next Greater Element.


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []

        def update():
            for i in range(len(nums)-1, -1, -1):
                while stack and nums[i] >= nums[stack[-1]]:
                    stack.pop()
                if stack:
                    res[i] = nums[stack[-1]]
                stack.append(i)

        update() # first pass
        update() # correct it on the 2nd pass with the same stack

        return res
"""
