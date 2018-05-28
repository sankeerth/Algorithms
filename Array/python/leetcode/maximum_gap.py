"""
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""
from math import ceil


class Solution(object):
    """
    Suppose there are N elements in the array, the min value is min and the max value is max.
    Then the maximum gap will be no smaller than ceiling[(max - min ) / (N - 1)].
    Let gap = ceiling[(max - min ) / (N - 1)]. We divide all numbers in the array into n-1 buckets,
    where k-th bucket contains all numbers in [min + (k-1)gap, min + k*gap). Since there are n-2 numbers that are not
    equal min or max and there are n-1 buckets, at least one of the buckets are empty.
    We only need to store the largest number and the smallest number in each bucket.
    After we put all the numbers into the buckets. We can scan the buckets sequentially and get the max gap.
    """
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0

        max_gap = 0
        min_num = min(nums)
        max_num = max(nums)
        if max_num == min_num:
            return 0
        min_gap = (max_num-min_num)/(length-1)
        buckets_min = [float('inf')] * length
        buckets_max = [float('-inf')] * length

        for num in nums:
            bucket_index = round((num - min_num) / min_gap)
            buckets_min[bucket_index] = min(num, buckets_min[bucket_index])
            buckets_max[bucket_index] = max(num, buckets_max[bucket_index])

        max_elem = buckets_max[0]

        for i in range(1, length):
            min_elem = buckets_min[i]
            if min_elem == float('inf'):
                continue
            max_gap = max(max_gap, min_elem - max_elem)
            max_elem = min_elem

        return max_gap


sol = Solution()
print(sol.maximumGap([2, 4, 6, 8]))
print(sol.maximumGap([2, 7, 4, 5, 6]))
print(sol.maximumGap([2, 7, 4]))
print(sol.maximumGap([2, 7]))
print(sol.maximumGap([1, 2, 3, 53]))
print(sol.maximumGap([1, 1, 1, 1]))
print(sol.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]))
print(sol.maximumGap([12115,10639,2351,29639,31300,11245,16323,24899,8043,4076,17583,15872,19443,12887,5286,6836,31052,25648,17584,24599,13787,24727,12414,5098,26096,23020,25338,28472,4345,25144,27939,10716,3830,13001,7960,8003,10797,5917,22386,12403,2335,32514,23767,1868,29882,31738,30157,7950,20176,11748,13003,13852,19656,25305,7830,3328,19092,28245,18635,5806,18915,31639,24247,32269,29079,24394,18031,9395,8569,11364,28701,32496,28203,4175,20889,28943,6495,14919,16441,4568,23111,20995,7401,30298,2636,16791,1662,27367,2563,22169,1607,15711,29277,32386,27365,31922,26142,8792]))
