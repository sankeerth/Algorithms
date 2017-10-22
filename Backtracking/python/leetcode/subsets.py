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


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]

        result = list()
        nums.sort(reverse=True)

        def subsets_recr(nums):
            if len(nums) == 1:
                result.append(list(nums))
            else:
                subsets_recr(nums[1:])
                for i in range(len(result)):
                    l = list(result[i])
                    l.append(nums[0])
                    result.append(l)
                result.append([nums[0]])

        subsets_recr(nums)
        result.append([])

        return result

sol = Solution()
print(sol.subsets([]))
print(sol.subsets([1,2,3,4]))
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
"""