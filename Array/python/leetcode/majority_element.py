"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        majority_element = 0

        for num in nums:
            if count == 0:
                majority_element = num
                count += 1
            else:
                if num == majority_element:
                    count += 1
                else:
                    count -= 1

        if count == 0:
            return -1

        count = 0
        for num in nums:
            if num == majority_element:
                count += 1

        if count > int(len(nums) / 2):
            return majority_element
        else:
            return -1

sol = Solution()
print(sol.majorityElement([1]))
print(sol.majorityElement([2,2,2,3,4,5,2,2,5]))
print(sol.majorityElement([2,4,2,5,3]))
print(sol.majorityElement([5,2,4,2,1,2,2,3,2,1]))
