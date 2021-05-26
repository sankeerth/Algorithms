"""
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        if not nums:
            return 1

        if len(nums) == 1:
            return 2 if nums[0] == 1 else 1

        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if int(nums[i] / n) == 0:
                return i
        return n


sol = Solution()
print(sol.firstMissingPositive([1, 1, 2, 2, 2, 3]))
print(sol.firstMissingPositive([1, 2, 0, 0, 4]))
print(sol.firstMissingPositive([2, 2]))
print(sol.firstMissingPositive([2, 1]))
print(sol.firstMissingPositive([3, 1]))
print(sol.firstMissingPositive([0, 3]))
print(sol.firstMissingPositive([3, 1, 2]))
print(sol.firstMissingPositive([3, 4, -1, 1]))
print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
print(sol.firstMissingPositive([0]))
print(sol.firstMissingPositive([1]))
print(sol.firstMissingPositive([2]))
print(sol.firstMissingPositive([-1]))


"""
My O(n) solution with in place modification:

Convert all numbers < 0 and > len to 1
Append 1 to end of list to take care of the integer equal to len
Negate the numbers to indicate the presence of a positive integer

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res, isOne = 1, False
        
        for i in range(len(nums)):
            if nums[i] == 1:
                isOne = True
            if nums[i] <= 0:
                nums[i] = 1

        if not isOne:
            return res

        nums.append(1)
        for i in range(len(nums)):
            index = abs(nums[i])
            if index < len(nums) and nums[index] > 0:
                nums[index] *= -1

        while res < len(nums):
            if nums[res] > 0:
                return res
            res += 1

        return res
"""
