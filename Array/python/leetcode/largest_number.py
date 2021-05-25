"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:
Input: nums = [1]
Output: "1"

Example 4:
Input: nums = [10]
Output: "10"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
from typing import List


class CustomCmp(object):
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        left = str(self.obj) + str(other.obj)
        right = str(other.obj) + str(self.obj)
        return int(left) < int(right)

    def __gt__(self, other):
        left = str(self.obj) + str(other.obj)
        right = str(other.obj) + str(self.obj)
        return int(left) > int(right)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_ints = sorted(nums, key=CustomCmp, reverse=True)
        sorted_ints_to_strings = [str(num) for num in sorted_ints]
        return ''.join(sorted_ints_to_strings) if sorted_ints_to_strings[0] != "0" else "0"


sol = Solution()
print(sol.largestNumber([3, 30, 34, 5, 9]))
print(sol.largestNumber([10, 2]))
print(sol.largestNumber([5, 60, 6]))
print(sol.largestNumber([0, 0]))
