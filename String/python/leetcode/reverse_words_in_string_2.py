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


class Solution:
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def swap(i, j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

        def reverse(i, j):
            while i < j:
                swap(i, j)
                i += 1
                j -= 1

        reverse(0, len(s)-1)
        s.append(' ')
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(j, i-1)
                j = i+1

        s.pop()
        print(s)


sol = Solution()
sol.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
