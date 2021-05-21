"""
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers 
in nums such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff, result = float('inf'), float('inf')

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(target - total) < diff:
                    diff = abs(target - total)
                    result = total

                if result == target:
                    return result

                if total < target:
                    j += 1
                else:
                    k -= 1

        return result


s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
print(s.threeSumClosest([-1,2,1,-4], -5))
print(s.threeSumClosest([-1,2,1,-4], -4))
print(s.threeSumClosest([-1,2,1,-4], 2))
print(s.threeSumClosest([-1, -1, 2, 2, 0, 1, 2, -1, -4], 2))
print(s.threeSumClosest([-1, -1, 2, 2, 0, 1, 2, -1, -4], 4))
print(s.threeSumClosest([-1, -1, 2, 2, 0, 1, 2, -1, -4], 11))
print(s.threeSumClosest([-1, -1, 2, 2, 0, 1, 2, -1, -4], 0))
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
