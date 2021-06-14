"""
1400. Construct K Palindrome Strings

Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Example 4:
Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.

Example 5:
Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.

Constraints:
1 <= s.length <= 10^5
All characters in s are lower-case English letters.
1 <= k <= 10^5
"""
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        oddCount = 0
        counter = Counter(s)

        for count in counter.values():
            if count % 2 != 0:
                oddCount += 1

        return True if oddCount <= k else False


sol = Solution()
print(sol.canConstruct("annabelle", 2))
print(sol.canConstruct("leetcode", 3))
print(sol.canConstruct("true", 4))
print(sol.canConstruct("yzyzyzyzyzyzyzy", 2))
print(sol.canConstruct("cr", 2))


"""
Leetcode discuss solution using XOR:

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        odd = 0
        counter = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            counter[index] ^= 1
            odd = odd + 1 if counter[index] > 0 else odd - 1

        return odd <= k
"""
