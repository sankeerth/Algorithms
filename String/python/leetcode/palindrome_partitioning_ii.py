"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1

Constraints:
1 <= s.length <= 2000
s consists of lower-case English letters only.
"""


class Solution:
    def minCut(self, s: str) -> int:
        if not s : return 0
        
        cuts = [float('inf')] * len(s)
        dp = [[False] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            cuts[i] = i
            for j in range(i+1):
                if s[j] == s[i] and (i-j < 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if j == 0:
                        cuts[i] = 0
                    else:
                        cuts[i] = min(cuts[i], cuts[j-1]+1)

        return cuts[-1]


s = Solution()
print(s.minCut("aab"))
print(s.minCut("a"))
print(s.minCut("ab"))
print(s.minCut("abbabb"))
print(s.minCut("aabbcc"))
print(s.minCut("aabb"))


"""
Without memoization/DP:

class Solution:
    def minCut(self, s: str) -> int:
        result = float('inf')
        dp = [[False] * len(s) for i in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        def minCutRecursive(i, l, cuts):
            nonlocal result
            if dp[i][l]:
                result = min(result, cuts)
            else:
                for j in range(i, l):
                    if i == j or dp[i][j]:
                        minCutRecursive(j+1, l, cuts+1)

        minCutRecursive(0, len(s)-1, 0)
        return result
"""
