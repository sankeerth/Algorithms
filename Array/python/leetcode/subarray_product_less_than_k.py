"""
713. Subarray Product Less Than K

Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of 
all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j, res = 0, 0, 0
        product = 1

        while j < len(nums):
            product *= nums[j]
            while product >= k and i <= j:
                product /= nums[i]
                i += 1
            
            res += j-i+1
            j += 1

        return res


sol = Solution()
print(sol.numSubarrayProductLessThanK([10, 12, 5, 2], 10))
print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(sol.numSubarrayProductLessThanK([10, 5, 3, 3, 4, 2, 1], 10))
print(sol.numSubarrayProductLessThanK([10, 5, 3, 3, 12, 4, 2, 1], 10))
print(sol.numSubarrayProductLessThanK([1, 1, 1, 1, 1, 11], 10))


"""
Leetcode solution: Binary Search on Logarithms

Because log(∏i​xi​)=∑i​logxi​, we can reduce the problem to subarray sums instead of 
subarray products. The motivation for this is that the product of some arbitrary subarray 
may be way too large (potentially 1000^50000), and also dealing with sums gives us some 
more familiarity as it becomes similar to other problems we may have solved before.

Algorithm
After this transformation where every value x becomes log(x), let us take prefix sums 
prefix[i+1] = nums[0] + nums[1] + ... + nums[i]. Now we are left with the problem of finding, 
for each i, the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k.

Because prefix is a monotone increasing array, this can be solved with binary search. 
We add the width of the interval [i, j] to our answer, which counts all subarrays [i, k] with k <= j.

class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k == 0) return 0;
        double logk = Math.log(k);
        double[] prefix = new double[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i+1] = prefix[i] + Math.log(nums[i]);
        }

        int ans = 0;
        for (int i = 0; i < prefix.length; i++) {
            int lo = i + 1, hi = prefix.length;
            while (lo < hi) {
                int mi = lo + (hi - lo) / 2;
                if (prefix[mi] < prefix[i] + logk - 1e-9) lo = mi + 1;
                else hi = mi;
            }
            ans += lo - i - 1;
        }
        return ans;
    }
}
"""
