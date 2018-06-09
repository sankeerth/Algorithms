"""
583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

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
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = [[float('inf')] * (len(word2)+1) for _ in range(len(word1)+1)]

        def min_distance_recr(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            elif dp[i][j] != float('inf'):
                return dp[i][j]
            elif i == len(word1):
                dp[i][j] = len(word2) - j
                return len(word2) - j
            elif j >= len(word2):
                dp[i][j] = len(word1) - i
                return len(word1) - i

            if word1[i] == word2[j]:
                dp[i][j] = min_distance_recr(i+1, j+1)
            else:
                dp[i][j] = min(min_distance_recr(i+1, j), min_distance_recr(i, j+1)) + 1

            return dp[i][j]

        return min_distance_recr(0, 0)
'''
