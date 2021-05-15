"""
940. Distinct Subsequences II

Given a string s, count the number of distinct, non-empty subsequences of s .
Since the result may be large, return the answer modulo 109 + 7.

Example 1:
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".

Example 3:
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Note:
s contains only lowercase letters.
1 <= s.length <= 2000
"""

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        lastSeen = {}

        for i, c in enumerate(s):
            if c in lastSeen:
                lastSeenIndex = lastSeen[c]
                dp[i+1] = dp[i] * 2 - dp[lastSeenIndex]
            else:
                dp[i+1] = dp[i] * 2
            lastSeen[c] = i

        return (dp[len(s)]-1) % (10**9 + 7)


s = Solution()
print(s.distinctSubseqII("aba"))
print(s.distinctSubseqII("abb"))
print(s.distinctSubseqII("abc"))
print(s.distinctSubseqII("aaaa"))
print(s.distinctSubseqII("abaaa"))
print(s.distinctSubseqII("zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn"))
