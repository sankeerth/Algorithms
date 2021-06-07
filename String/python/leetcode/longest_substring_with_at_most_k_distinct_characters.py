"""
340. Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:
1 <= s.length <= 5 * 104
0 <= k <= 50
"""
from typing import List
from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter(s)
        if k >= len(counter):
            return len(s)
        
        for char in counter:
            counter[char] = 0

        res, count, l = 0, 0, 0
        for r in range(len(s)):
            char = s[r]
            if not counter[char]:
                count += 1
            counter[char] += 1

            while count > k:
                counter[s[l]] -= 1
                if not counter[s[l]]:
                    count -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res


sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))
print(sol.lengthOfLongestSubstringKDistinct("aa", 1))
