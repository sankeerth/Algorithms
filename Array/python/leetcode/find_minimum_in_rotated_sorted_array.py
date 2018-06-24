"""
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        return nums[lo]


sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
print(sol.findMin([6, 7, 0, 1, 2, 3, 4, 5]))
print(sol.findMin([6, 0, 1, 2, 3, 4, 5]))
print(sol.findMin([0, 1, 2, 3, 4, 5, 6]))
print(sol.findMin([3, 4, 5, 6, 7, 0, 1, 2]))
print(sol.findMin([1, 2]))
print(sol.findMin([2, 1]))

"""
Leetcode discuss solution:

Looking at subarray with index [start,end]. We can find out that if the first member is less than the last member, 
there's no rotation in the array. So we could directly return the first element in this subarray.

If the first element is larger than the last one, then we compute the element in the middle, and compare it with the 
first element. If value of the element in the middle is larger than the first element, we know the rotation is at 
the second half of this array. Else, it is in the first half in the array.

int findMin(vector<int> &num) {
    int start=0,end=num.size()-1;
    
    while (start<end) {
        if (num[start]<num[end])
            return num[start];
        
        int mid = (start+end)/2;
        
        if (num[mid]>=num[start]) {
            start = mid+1;
        } else {
            end = mid;
        }
    }
    
    return num[start];
}
"""
