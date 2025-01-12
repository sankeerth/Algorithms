"""
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum = float('inf')
        secondNum = float('inf')

        for num in nums:
            # it is ok to update the first and second num since the update is on less than or equal to, hence there is a bigger number in the lower index
            # however, if you want all three numbers that satisfy this condition then just returning the first, second and third num wouldn't work 
            if num <= firstNum:
                firstNum = num
            elif num <= secondNum:
                secondNum = num
            else:
                return True

        return False


sol = Solution()
print(increasingTriplet([1,2,3,4,5]))
print(increasingTriplet([5,4,3,2,1]))
print(increasingTriplet([2,1,5,0,4,6]))
print(increasingTriplet([3,9,4,6]))
print(increasingTriplet([5,7,9,4,6]))
print(increasingTriplet([3,4,1,2,3]))
