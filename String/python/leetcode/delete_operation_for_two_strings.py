"""
583. Delete Operation for Two Strings

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word1) + 1):
            dp[0][i] = i

        for i in range(len(word2) + 1):
            dp[i][0] = i

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] != word1[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]

        return dp[len(word2)][len(word1)]


sol = Solution()
print(sol.minDistance("sea", "eat"))
print(sol.minDistance("sea", "e"))
print(sol.minDistance("sea", "tea"))
print(sol.minDistance("eea", "eae"))
print(sol.minDistance("sea", "xyz"))
print(sol.minDistance("abcdef", "afbc"))
print(sol.minDistance("s", ""))
print(sol.minDistance("", ""))


"""
Leetcode discuss solution:
To make them identical, just find the longest common subsequence. The rest of the characters have to be deleted from 
the both the strings, which does not belong to longest common subsequence.

public int minDistance(String word1, String word2) {
    int dp[][] = new int[word1.length()+1][word2.length()+1];
    for(int i = 0; i <= word1.length(); i++) {
        for(int j = 0; j <= word2.length(); j++) {
            if(i == 0 || j == 0) 
                dp[i][j] = 0;
            else 
                dp[i][j] = (word1.charAt(i-1) == word2.charAt(j-1)) ? dp[i-1][j-1] + 1
                    : Math.max(dp[i-1][j], dp[i][j-1]);
        }
    }
    int val =  dp[word1.length()][word2.length()];
    return word1.length() - val + word2.length() - val;
}
"""

'''
My dp recursive (top-down) solution:

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def minDistanceRecursive(i, j):
            if i == len(word1) or j == len(word2):
                return max(len(word1)-i, len(word2)-j)
            elif (i, j) in memo:
                return memo[(i, j)]
            elif word1[i] == word2[j]:
                memo[(i, j)] = minDistanceRecursive(i+1, j+1)
            else:
                memo[(i, j)] = 1 + min(minDistanceRecursive(i+1, j), minDistanceRecursive(i, j+1))

            return memo[(i, j)]

        return minDistanceRecursive(0, 0)
'''
