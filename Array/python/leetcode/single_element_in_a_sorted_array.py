"""
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if mid % 2 != 0:
                if nums[mid] == nums[mid-1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[mid] == nums[mid-1]:
                    hi = mid
                else:
                    lo = mid
        
        return nums[lo]


sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))
print(sol.singleNonDuplicate([1,2,2]))
print(sol.singleNonDuplicate([1,1,2]))
print(sol.singleNonDuplicate([2,3,3,7,7,11,11]))


"""
Leetcode solution:

'''
We need to make sure our mid index is even. We can do this by dividing lo and hi in the usual way, but then decrementing it by 1 if it is odd. 
This also ensures that if we have an even number of even indexes to search, that we are getting the lower middle (incrementing by 1 here would not work, 
it'd lead to an infinite loop as the search space would not be reduced in some cases).

Then we check whether or not the mid index is the same as the one after it.

If it is, then we know that mid is not the single element, and that the single element must be at an even index after mid. Therefore, we set lo to be mid + 2. 
It is +2 rather than the usual +1 because we want it to point at an even index.
If it is not, then we know that the single element is either at mid, or at some index before mid. Therefore, we set hi to be mid.
Once lo == hi, the search space is down to 1 element, and this must be the single element, so we return it.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]
"""
