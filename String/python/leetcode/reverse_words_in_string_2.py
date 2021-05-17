"""
186. Reverse Words in a String II

Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""
from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        reverse(0, len(s)-1)
        i, start = 0, 0
        while i < len(s):
            if s[i] == ' ':
                reverse(start, i-1)
                start = i+1
            i += 1

        reverse(start, i-1)
        # print(s)


sol = Solution()
sol.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
sol.reverseWords(["t","h","e"," ","n","e","w"," ","y","o","r","k"])
