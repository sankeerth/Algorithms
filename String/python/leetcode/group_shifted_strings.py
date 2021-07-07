"""
249. Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. 
You may return the answer in any order.

Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]

Constraints:
1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for string in strings:
            if len(string) == 1:
                hashMap[-1].append(string)
                continue
            
            total = []
            for i in range(1, len(string)):
                p = ord(string[i-1]) - ord('a')
                n = ord(string[i]) - ord('a')
                
                c = (n-p) % 26
                total.append(str(c))
            
            key = "|".join(total)
            hashMap[key].append(string)
            
        return list(hashMap.values())


sol = Solution()
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
print(sol.groupStrings(["a"]))
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z","aa","bb"]))
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z","yza","zab"]))
# failed testcases
print(sol.groupStrings(["aa","bb","ccc"]))
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z","al"]))
