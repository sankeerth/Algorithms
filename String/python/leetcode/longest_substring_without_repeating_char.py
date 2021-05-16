"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
from collections import deque, defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue, uniques = [], set()
        res = 0

        for c in s:
            if c in uniques:
                while queue:
                    top = queue.pop(0)
                    uniques.remove(top)
                    if top == c:
                        break
            queue.append(c)
            uniques.add(c)
            res = max(res, len(queue))

        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("azbckbc"))


"""
the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values, and keep two pointers which define the max substring.
move the right pointer to scan through the string , and meanwhile update the hashmap. If the character is already in the hashmap, then move the left pointer to the right of the same character last found.
Note that the two pointers can only move forward.

int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
}

Python code for the same:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurances = {}
        start, res = -1, 0

        for i in range(len(s)):
            if s[i] in occurances and occurances[s[i]] > start:
                start = occurances[s[i]]
            occurances[s[i]] = i
            res = max(res, i - start)

        return res
"""
