"""
727. Minimum Window Subsequence

Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.
If there is no such window in s1 that covers all characters in s2, return the empty string "". 
If there are multiple such minimum-length windows, return the one with the left-most starting index. 

Example 1:
Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.

Example 2:
Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""

Constraints:
1 <= s1.length <= 2 * 104
1 <= s2.length <= 100
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        dp = [[float('inf')] * len(s1) for _ in range(len(s2))]
        if s1[0] == s2[0]:
            dp[0][0] = 1

        for i in range(1, len(s1)):
            if s1[i] == s2[0]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1] + 1
        
        for i in range(1, len(s2)):
            for j in range(1, len(s1)):
                if s2[i] == s1[j] and dp[i-1][j-1] != float('inf'): # Before failed testcase: `if s2[i] == s1[j]: dp[i][j] = dp[i-1][j]`
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = dp[i][j-1] + 1

        resArray = dp[len(s2)-1]
        minVal = min(resArray)
        index = resArray.index(minVal)
        
        if minVal == float('inf'):
            subsequence = ""
        else:
            subsequence = s1[index-minVal+1: index+1]
        return subsequence


sol = Solution()
print(sol.minWindow("abcdebde", "bde"))
print(sol.minWindow("cnhczmccqouqadqtmjjzl", "mm"))


"""
Leetcode discuss solution:
Stores that start index in dp array instead of my implementation above where I store the length

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = j + 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        start, minLen = 0, float('inf')
        for j in range(1, n + 1):
            if dp[m][j] > 0:
                if j - dp[m][j] + 1 < minLen:
                    minLen = j - dp[m][j] + 1 
                    start = dp[m][j] - 1

        return "" if minLen == float('inf') else s1[start: start + minLen]
"""
