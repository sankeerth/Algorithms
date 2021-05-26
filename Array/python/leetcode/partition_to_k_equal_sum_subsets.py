"""
698. Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, find whether it's possible 
to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):
            return False
        
        s, m = sum(nums), max(nums)
        if s % k != 0:
            return False

        target = int(sum(nums) / k)
        if m > target:
            return False
        
        nums.sort(reverse=True)
        bucket = [target] * k
        def dfs(pos):
            if pos == len(nums):
                return True
            
            for i in range(k):
                if bucket[i] >= nums[pos]:
                    bucket[i] -= nums[pos]
                    if dfs(pos+1):
                        return True
                    bucket[i] += nums[pos]

            return False

        return dfs(0)


s = Solution()
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)) # True
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 5)) # False
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 2], 4)) # False
print(s.canPartitionKSubsets([4,4,4,4], 4)) # True
print(s.canPartitionKSubsets([4,4,4,4], 2)) # True
print(s.canPartitionKSubsets([4,4,4,4], 8)) # False
print(s.canPartitionKSubsets([6,6], 3)) # False
print(s.canPartitionKSubsets([4, 1, 2, 4], 2)) # False
print(s.canPartitionKSubsets([4, 1, 2, 4], 1)) # True
print(s.canPartitionKSubsets([3,3,3,3,3,3], 2)) # True
print(s.canPartitionKSubsets([1,2,2,2,4,1], 2)) # True
print(s.canPartitionKSubsets([1,2,2,2,4,1,2,6], 2)) # True
print(s.canPartitionKSubsets([1,2,2,2,4,1,2,7,5], 2)) # True
print(s.canPartitionKSubsets([5,3,1,1,7,2,1,10], 3)) # True
print(s.canPartitionKSubsets([5,3,1,1,7,2,1,10,3], 3)) # True
print(s.canPartitionKSubsets([2,2,2,2,3,4,5], 4)) # False
print(s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3)) # True


"""
Using the set()/visited approach that I had in mind:

public boolean canPartitionKSubsets(int[] nums, int k) {
    int sum = 0;
    for(int num:nums)sum += num;
    if(k <= 0 || sum%k != 0)return false;
    int[] visited = new int[nums.length];
    return canPartition(nums, visited, 0, k, 0, 0, sum/k);
}

public boolean canPartition(int[] nums, int[] visited, int start_index, int k, int cur_sum, int cur_num, int target){
    if(k==1)return true;
    if(cur_sum == target && cur_num>0)return canPartition(nums, visited, 0, k-1, 0, 0, target);
    for(int i = start_index; i<nums.length; i++){
        if(visited[i] == 0){
            visited[i] = 1;
            if(canPartition(nums, visited, i+1, k, cur_sum + nums[i], cur_num++, target))return true;
            visited[i] = 0;
        }
    }
    return false;
}
"""

"""
Check DP Bitmask solution later:
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/335668/DP-with-Bit-Masking-Solution-%3A-Best-for-Interviews

public boolean canPartitionKSubsets(int[] nums, int k) {
		if(nums == null || nums.length == 0)
			return false;
		
		int n = nums.length;
		//result array
		boolean dp[] = new boolean[1<<n];
		int total[] = new int[1<<n];
		dp[0] = true;
		
		int sum = 0;
		for(int num : nums)
			sum += num;
		Arrays.sort(nums);
		
		if(sum%k != 0) 
			return false;
		sum /= k;
		if(nums[n-1] > sum)
			return false;
		// Loop over power set
		for(int i = 0;i < (1<<n);i++) {
			if(dp[i]) {
				// Loop over each element to find subset
				for(int j = 0;j < n;j++) {
					// set the jth bit 
					int temp = i | (1 << j);
					if(temp != i) {
						// if total sum is less than target store in dp and total array
						if(nums[j] <= (sum- (total[i]%sum))) {
							dp[temp] = true;
							total[temp] = nums[j] + total[i];
						} else
							break;
					}
				}
			}
		}
		return dp[(1<<n) - 1];
	}
"""
