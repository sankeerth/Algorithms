"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = nums[0], 0
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == majority:
                count += 1

        return majority if count > len(nums) / 2 else -1


sol = Solution()
print(sol.majorityElement([1]))
print(sol.majorityElement([2,2,2,3,4,5,2,2,5]))
print(sol.majorityElement([2,4,2,5,3]))
print(sol.majorityElement([2,4,2,5,2,3]))
print(sol.majorityElement([2,4,2,5,3,2]))
print(sol.majorityElement([5,2,4,2,1,2,2,3,2,1]))


"""
Divide conquer solution with O(n logn) time complexity:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majorityElementRecurisve(lo, hi):
            if lo >= hi:
                return nums[lo]
            
            mid = (lo + hi) // 2
            left = majorityElementRecurisve(lo, mid)
            right = majorityElementRecurisve(mid+1, hi)

            if left == right:
                return left

            leftCount, rightCount = 0, 0
            for i in range(lo, hi+1):
                if nums[i] == left:
                    leftCount += 1
                elif nums[i] == right:
                    rightCount += 1

            # This code can be used to return -1 when there is no majority element
            # majority = (hi - lo + 1) / 2
            # if leftCount <= majority and rightCount <= majority:
            #     return -1

            return left if leftCount > rightCount else right
        
        return majorityElementRecurisve(0, len(nums)-1)
"""
