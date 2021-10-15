"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).
You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. 
The difficulty of a day is the maximum difficulty of a job done in that day.
Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].
Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""

from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if not jobDifficulty:
            return 0

        length = len(jobDifficulty)
        if length < d:
            return -1

        dp = [[float('inf')] * (length+1) for i in range(d+1)]
        dp[0][0] = 0 # The minimum difficulty on day 0 to get 0 job done is 0

        for i in range(1, d+1): # starting from day 1
            # j starts from i because at least j-1 jobs must be done in i-1 days or at least 1 job done on ith day
            # length - j >= d - i means we need to leave enough jobs for rest of days
            # length - j is the jobs left and d - i is the days left

            j = i
            while (length-j) >= (d-i):
                currMax = jobDifficulty[j-1]
                k = i-1
                while k <= j-1:
                    currMax = max(jobDifficulty[k], currMax)
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + currMax)
                    k += 1
                j += 1

        return dp[d][length]  


s = Solution()
#print(s.minDifficulty([7,1,7,1,7,1], 3))
# print(s.minDifficulty([1,1,1], 3))
# print(s.minDifficulty([9,9,9], 4))
#print(s.minDifficulty([6,5,4,3,2,1], 3))
print(s.minDifficulty([7,1,7,1], 2))
# print(s.minDifficulty([11,111,22,222,33,333,44,444], 6))
#print(s.minDifficulty([380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315], 10))


'''
Very good explanation:
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/924611/DFS-greater-DP-Progression-with-Explanation-O(n2d)O(nd)

Each step down the tree partitions one of the segments into two. In code, this would look like

def dfs(jobs, d):
	if d == 1:
		return max(jobs)
	minDiff = float("inf")
	for i in range(1, len(jobs)):
		curr = max(jobs[:i]) + dfs(jobs[i:], d - 1)
		minDiff = min(minDiff, curr)
	return minDiff
return dfs(jobDifficulty, d)
This is a standard tree traversal, where at each node, we acquire some cost m(...), and then continue down the tree until we hit the base case (if d == 1: return max(jobs)). Therefore, we are looking for the minimum cost root -> leaf path of length d. This DFS approach solves the problem, however for larger inputs it takes far too long and times out. Why is that? Notice in the DFS tree, we have the two recursive calls

m(a) + m(b) + dfs(cd)
m(a, b) + dfs(cd)

https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/932073/Java-Recursion-%2B-Memoization
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/907494/Java-DP-solution-with-detailed-explanation
'''

# 3rd leetcode link. Did not quite understand the dp formula
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if not jobDifficulty:
            return 0

        length = len(jobDifficulty)
        if length < d:
            return -1

        dp = [[float('inf')] * (length+1) for i in range(d+1)]
        dp[0][0] = 0 # The minimum difficulty on day 0 to get 0 job done is 0

        for i in range(1, d+1): # starting from day 1
            # j starts from i because at least j-1 jobs must be done in i-1 days or at least 1 job done on ith day
            # length - j >= d - i means we need to leave enough jobs for rest of days
            # length - j is the jobs left and d - i is the days left

            j = i
            while (length-j) >= (d-i):
                currMax = jobDifficulty[j-1]
                k = i-1
                while k <= j-1:
                    currMax = max(jobDifficulty[k], currMax)
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + currMax)
                    k += 1
                j += 1

        return dp[d][length]  
'''

# My recursive solution without dp
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if not jobDifficulty or d > len(jobDifficulty):
            return -1

        # initialize
        length = len(jobDifficulty)
        maxOfIToJ = [[0] * length for i in range(length)]

        # fill 2d array with max values until j'th index so max(i,j) can be O(1)
        for i in range(length):
            maxOfIToJ[i][i] = jobDifficulty[i]

        # calculate the max of all indices (i..j)
        for i in range(length):
            for j in range(i+1, length):
                maxOfIToJ[i][j] = max(jobDifficulty[j], maxOfIToJ[i][j-1])

        result = float('inf')
        def minDifficultyRecursive(start, currrentDay, difficulty):
            print(start, currrentDay)
            nonlocal result
            if currrentDay == d:
                result = min(result, difficulty + maxOfIToJ[start][length-1])
                return
            for i in range(start, length-d+currrentDay):
                difficulty += maxOfIToJ[start][i]
                minDifficultyRecursive(i+1, currrentDay+1, difficulty)
                difficulty -= maxOfIToJ[start][i]

        minDifficultyRecursive(0, 1, 0)

        return result
'''
