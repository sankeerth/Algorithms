"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from collections import deque, defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        if len(s) == 1:
            return 1

        length = len(s)

        dq = deque()
        char_dict = defaultdict(int)
        max_length = 0
        dq.append(s[0])
        char_dict[s[0]] = 1

        for i in range(1, length):
            if char_dict[s[i]]:
                while dq:
                    c = dq.popleft()
                    char_dict[c] = 0
                    if c == s[i]:
                        break
            char_dict[s[i]] = 1
            dq.append(s[i])

            max_length = max(len(dq), max_length)

        return max_length

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
"""
