"""
395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency 
of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        maxDistinct = len(set(s))

        def longestSubstringWithNDistinct(distinct):
            longest = 0
            counter = defaultdict(int)
            left, right = 0, 0
            curDistinct, countAtLeastK = 0, 0

            while right < len(s):
                char = s[right]
                if not counter[char]:
                    curDistinct += 1
                counter[char] += 1

                if counter[char] == k:
                    countAtLeastK += 1
                
                while curDistinct > distinct:
                    char = s[left]
                    counter[char] -= 1
                    if not counter[char]:
                        curDistinct -= 1
                    if counter[char] == k-1:
                        countAtLeastK -= 1
                    left += 1
            
                if curDistinct == countAtLeastK:
                    longest = max(longest, right-left+1)
                right += 1
            
            return longest

        for distinct in range(1, maxDistinct+1):
            longest = longestSubstringWithNDistinct(distinct)
            res = max(res, longest)

        return res


sol = Solution()
print(sol.longestSubstring("ababbc", 2))
print(sol.longestSubstring("cababbc", 2))
print(sol.longestSubstring("cababb", 2))
print(sol.longestSubstring("aaabb", 3))
print(sol.longestSubstring("baaabb", 3))
print(sol.longestSubstring("baaab", 3))
