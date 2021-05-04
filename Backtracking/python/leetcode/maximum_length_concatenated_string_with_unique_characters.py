"""
1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence 
of arr which have unique characters. Return the maximum possible length of s.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0
        uniques = []

        for word in arr:
            s = set(word)
            if len(s) == len(word):
                for unique in uniques:
                    if not s.intersection(unique):
                        union = s.union(unique)
                        result = max(result, len(union))
                        uniques.append(union)
                
                uniques.append(s)
                result = max(result, len(s))

        return result


s = Solution()
print(s.maxLength(["cha","r","act","ers"]))
print(s.maxLength(["un","iq","ue"]))
print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(s.maxLength(["ar"]))
print(s.maxLength(["aa"]))
print(s.maxLength([""]))

"""
Backtracking solution:

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniques = [set(word) for word in arr if len(word) == len(set(word))]

        def backtrack(i, uniqueSet):
            if i == len(uniques):
                return len(uniqueSet)
            
            withCurrent = 0
            if not uniques[i] & uniqueSet:
                withCurrent = backtrack(i+1, uniques[i] | uniqueSet)

            withoutCurrent = backtrack(i+1, uniqueSet)
            return max(withCurrent, withoutCurrent)

        return backtrack(0, set())
"""
