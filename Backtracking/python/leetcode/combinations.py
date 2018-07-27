"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = list()

        def combine_recursive(i, temp):
            if k == len(temp):
                result.append(list(temp))
            else:
                for j in range(i, n+1):
                    temp.append(j)
                    combine_recursive(j+1, temp)
                    temp.pop()

        combine_recursive(1, list())
        return result


sol = Solution()
print(sol.combine(4, 2))
print(sol.combine(4, 0))
print(sol.combine(3, 1))
print(sol.combine(3, 3))


"""
Leetcode discuss solution:

class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        v.resize(k);
        dfs(1, n, k);
        return r;
    }
private:
    vector<vector<int> > r;
    vector<int> v;
    void dfs(int i, int n, int k) {
        while (i <= n) {
            v[v.size() - k] = i++;
            if (k > 1)
                dfs(i, n, k - 1);
            else
                r.push_back(v);
        }
    }
};
"""