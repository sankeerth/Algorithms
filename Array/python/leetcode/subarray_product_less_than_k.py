"""
713. Subarray Product Less Than K


Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, j = 0, 0
        current_prod = 1
        result = 0

        while j < len(nums):
            if nums[j] >= k:
                current_prod = 1
                result += ((j-i)*(j-i+1))/2
                j += 1
                i = j
            else:
                current_prod = current_prod * nums[j]
                if current_prod >= k:
                    while i < j and current_prod >= k:
                        result += (j-i)
                        current_prod = current_prod / nums[i]
                        i += 1
                j += 1

        result += ((j-i)*(j-i+1))/2

        return int(result)


sol = Solution()
print(sol.numSubarrayProductLessThanK([10, 12, 5, 2], 10))
print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(sol.numSubarrayProductLessThanK([10, 5, 3, 3, 4, 2, 1], 10))
print(sol.numSubarrayProductLessThanK([10, 5, 3, 3, 12, 4, 2, 1], 10))
print(sol.numSubarrayProductLessThanK([1, 1, 1, 1, 1, 11], 10))


'''
A little more elegant leetcode solution:

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k == 0) return 0;
        int cnt = 0;
        int pro = 1;
        for (int i = 0, j = 0; j < nums.size(); j++) {
            pro *= nums[j];
            while (i <= j && pro >= k) {
                pro /= nums[i];
                i ++;
            }
            cnt += j - i + 1;
        }
        return cnt;
    }
};
'''