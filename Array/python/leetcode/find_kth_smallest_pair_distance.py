"""
719. Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
"""


class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        A simple solution for this one could be O(n^2) by finding all possible combinations.
        This code is from leetcode discuss solution:
        A key thing to note while performing binary search is to figure out "search space", which can be in the form of
        an "index" or "range". Here, we use "range" as the search space for finding "mid"

        low = min_diff_between_all_nums
        high = a[n - 1] - a[0]
        all possible sums are in between low and high
        binary search tries to find such distance that amount of smaller distances are not greater than k.
        count_pairs(arr, mid) < k means mid distance is too small, we need a bigger one, so we go right
        count_pairs(arr, mid) >= k means mid distance is big enough, but can be smaller
        by the end of binary search we will have the exact distance equal to low such that number of smaller distances
        is not greater than k
        """
        nums = sorted(nums)
        length = len(nums)
        lo, hi, result = 0, nums[length-1] - nums[0], 0

        while lo <= hi:
            mid = int(lo + (hi - lo)/2)
            cnt, j = 0, 0
            for i in range(length):
                while j < length and (nums[j] - nums[i]) <= mid:
                    j += 1
                cnt += j - i - 1

            if cnt >= k:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return result


sol = Solution()
print(sol.smallestDistancePair([1, 4, 2, 3], 6))
print(sol.smallestDistancePair([1, 4, 2, 3], 4))
print(sol.smallestDistancePair([1, 4, 2, 3], 2))
print(sol.smallestDistancePair([1, 4, 2, 1], 4))


