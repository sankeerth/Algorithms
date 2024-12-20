"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        
        def recursive(i):
            res.append(list(cur))
            for j in range(i, len(nums)):
                cur.append(nums[j])
                recursive(j+1)
                cur.pop()

        recursive(0)
        return res


sol = Solution()
print(sol.subsets([]))
print(sol.subsets([1,2,3]))
print(sol.subsets([1,4,1,2]))


"""
Leetcode discuss: Iterative solution

This problem can also be solved iteratively. Take [1, 2, 3] in the problem statement as an example. The process of generating all the subsets is like:

Initially: [[]]
Adding the first number to all the existed subsets: [[], [1]];
Adding the second number to all the existed subsets: [[], [1], [2], [1, 2]];
Adding the third number to all the existed subsets: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

The code is as follows.

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> subs(1, vector<int>());
        for (int i = 0; i < nums.size(); i++) {
            int n = subs.size();
            for (int j = 0; j < n; j++) {
                subs.push_back(subs[j]);
                subs.back().push_back(nums[i]);
            }
        }
        return subs;
    }
};

Python Solution:

class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                sub = list(res[i])
                sub.append(num)
                res.append(sub)

        return res

"""

"""
Recursive approach of the above one:

class Solution(object):
    def subsets(self, nums):
        result = []
        def subsetsRecursive(nums):
            if not nums:
                result.append([])
                return

            subsetsRecursive(nums[1:])
            num = nums[0]
            for i in range(len(result)):
                newSubset = list(result[i])
                newSubset.append(num)
                result.append(newSubset)

        subsetsRecursive(nums[::-1])
        return result
"""

"""
Either include the digit or not. Similar idea to the above one but in recursion and without any bitwise operation.

class Solution(object):
    def subsets(self, nums):
        res = []
        def subsetsRecursive(i, sub):
            if i == len(nums):
                res.append(sub)
                return
            
            subsetsRecursive(i+1, sub)
            subsetsRecursive(i+1, [nums[i]] + sub)

        subsetsRecursive(0, [])
        return res
"""

"""
Leetcode discuss: Bit Manipulation

This is the most clever solution that I have seen. The idea is that to give all the possible subsets,
we just need to exhaust all the possible combinations of the numbers.
And each number has only two possibilities: either in or not in a subset. And this can be represented using a bit.
There is also another a way to visualize this idea.
That is, if we use the above example, 1 appears once in every two consecutive subsets,
2 appears twice in every four consecutive subsets, and 3 appears four times in every eight subsets,
shown in the following (initially the 8 subsets are all empty):

[], [], [], [], [], [], [], []
[], [1], [], [1], [], [1], [], [1]
[], [1], [2], [1, 2], [], [1], [2], [1, 2]
[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]

The code is as follows.

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int num_subset = pow(2, nums.size());
        vector<vector<int> > res(num_subset, vector<int>());
        for (int i = 0; i < nums.size(); i++)
            for (int j = 0; j < num_subset; j++)
                if ((j >> i) & 1)
                    res[j].push_back(nums[i]);
        return res;
    }
};

Python code for the same:

def subsets(nums):
    N = len(nums)
    result = [[] for i in range(2 ** N)]

    for i in range(N):
        for j in range(len(result)):
            if j >> i & 1:
                result[j].append(nums[i])

    return result
"""
